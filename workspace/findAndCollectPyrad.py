import os 
import csv 
import argparse
import pandas as pd 
import numpy as np 

from csv import reader, writer
from datetime import datetime, timedelta 


def str_to_bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in {'false', 'f', '0', 'no', 'n'}:
        return False
    elif value.lower() in {'true', 't', '1', 'yes', 'y'}:
        return True
    raise ValueError("{0} is not a valid boolean value".format(value))


parser = argparse.ArgumentParser(description='Search the project collect all pyrad analysis into one csv')


#optional arguments
parser.add_argument('-f',"--dateformat", help="Date format to search for i.e '%Y%m%d%H%M%S' ", type=str, nargs='?', default="%Y%m%d%H%M%S")
parser.add_argument('-w',"--within", help="Filter for Pyrad that were generated within x hours of today", type=int, nargs='?')
parser.add_argument('-d',"--duplicates", help="Allow duplicates of analyisis for roi within a session", nargs='?', default=False, type=str_to_bool)

arguments = parser.parse_args()

dateformat = arguments.dateformat 
hours = arguments.within
duplicatesAllowed = arguments.duplicates
now = datetime.now()
nowFilename = now.strftime("%Y-%m-%d_%H:%M:%S")

print("duplicates allowed: ", duplicatesAllowed)

#input folder location 
input = "/input/"

#output file location 
filename = "PyradData"+"Within_"+str(hours)+"hoursof_"+str(nowFilename)+".csv"
filepath = '/output/'+filename






firstTime = True 

csvList = [os.path.join(dp, f) for dp, dn, filenames in os.walk(input) for f in filenames if os.path.splitext(f)[1] == '.csv']


if not duplicatesAllowed: 
    sessionsDict = {} 

with open (filepath, 'w') as pyrad_csv:
    pyrad_csv_writer = writer(pyrad_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for csv in csvList:
        if "pyradiomics" in csv: 
            info = csv.split("-")
            print(info)
            if len(info)>=4: 
                date = info[3]
                session = info[0].split('/')[-1]
                subject = session.split('_')[0]

                if "{" in date: 
                    date = date[1:-1]

                date = datetime.strptime(date, dateformat)
                
                if not duplicatesAllowed:
                    if session not in sessionsDict:
                        sessionsDict[session] = []

                if now-timedelta(hours) <= date <= now+timedelta(hours):
                    # print("within ", hours, " hours")
                    pyradData = pd.read_csv(csv)
                    if firstTime: 
                        columns = pyradData.columns
                        columns = columns.insert(0, "session")
                        columns = columns.insert(0, "subject")
                        pyrad_csv_writer.writerow(columns)
                        firstTime = False


                    pyradData.insert(0, "session", session)
                    pyradData.insert(0, "subject", subject)

                    data = pyradData.iloc[0]

                    roiMaskName = data["Mask"]

                    if not duplicatesAllowed: 
                        if roiMaskName not in sessionsDict[session]:
                            sessionsDict[session].append(roiMaskName)
                            pyrad_csv_writer.writerow(data)
                    else: 
                        pyrad_csv_writer.writerow(data)
                        


                else: 
                    print(csv, " not within ", hours, " hours")





# ROIResizer-Container 

## Introduction

> This container goes through the entire project on XNAT and finds all ROI's analyises within a certain number of hours of today. It also lets you filter for whether to include duplicates of data as well. 

##  Design: 
  * Used python 
  * full list of packages needed: (listed within the Dockerfile.base)
    * csv
    * argparse 
    * pandas 
    * numpy
    
   
##  How to use:
  > All the scripts are located within the "workspace" dir - any edits you will need to make for your specific use case will be with "scale.py". Once edits are done run ./build.sh to build your docker container. Specifics to edit within docker are the Dockerfile.base file for naming the container, pushing to git and libraries used. If you want integration with XNAT navigate to the "xnat" folder and edit the command.json documentation available at @ https://wiki.xnat.org/container-service/making-your-docker-image-xnat-ready-122978887.html#MakingyourDockerImage%22XNATReady%22-installing-a-command-from-an-xnat-ready-image

  * NOTE this was designed to be generalized to most RT structs so it should work just fine on its own with the exception of the rtstruct upload part that is unique to XNAT 

## Running (ON XNAT): 
  * Navigate to the project on mirrir and click on "Run containers"
  * The container should show up as "Runs collectPyrad container with project mounted" and click it
  * Fill out necessary arguments and hit run

## Running in general: 
  * There are arguments needed to run this pipline which can be found within the findandCollectPyrad.py script 
  * There is an upload componenet unique to XNAT if you just want to run it without uploading you can comment out that component. 

## NOTES: 
  * Parts of the scripts within workspace were written with project specificity in mind so please keep that in mind as you use this code 
  * It is recommended that you have some experience working with docker and specficially building containers for xnat for this to work for your use cases 
  * If you just want to use the code for your own work without docker stuff just navigate to workspace copy the python files from it and edit them 
  
## Future:   

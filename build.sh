cp Dockerfile.base Dockerfile && \
./command2label.py ./xnat/command.json >> Dockerfile && \
docker build -t xnat/pyradcollector:t2.5 .
docker tag xnat/pyradcollector:t2.5 registry.nrg.wustl.edu/docker/nrg-repo/yash/pyradcollector:t2.5
rm Dockerfile

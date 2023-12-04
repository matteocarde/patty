#!/bin/bash
aws ecr get-login-password --region eu-south-1 | docker login --username AWS --password-stdin 775013819650.dkr.ecr.eu-south-1.amazonaws.com
docker build -t icr -f Dockerfile-icr .
docker tag icr:latest 775013819650.dkr.ecr.eu-south-1.amazonaws.com/icr:latest
docker push 775013819650.dkr.ecr.eu-south-1.amazonaws.com/icr:latest
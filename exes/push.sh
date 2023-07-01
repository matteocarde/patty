#!/bin/bash
aws ecr get-login-password --region eu-south-1 | docker login --username AWS --password-stdin 775013819650.dkr.ecr.eu-south-1.amazonaws.com
docker build -t patty .
docker tag patty:latest 775013819650.dkr.ecr.eu-south-1.amazonaws.com/patty:latest
docker push 775013819650.dkr.ecr.eu-south-1.amazonaws.com/patty:latest
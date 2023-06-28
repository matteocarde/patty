#!/bin/bash
#This commands runs docker adding volumes for rapid development
#the volume ads also the credentials for aws
docker run \
  -v $(pwd)/exes:/project/exes \
  -v $(pwd)/benchmarks:/project/benchmarks \
  -v $HOME/.aws/credentials:/root/.aws/credentials \
  --platform linux/amd64 \
  -t -i patty $@
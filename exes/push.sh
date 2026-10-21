#!/bin/bash
set -euo pipefail

IMAGE="775013819650.dkr.ecr.eu-south-1.amazonaws.com/patty:latest"

if [ -n "$(git status --porcelain)" ]; then
  echo "You have to first commit to git in order to push to ecr";
  exit 1
fi
aws ecr get-login-password --region eu-south-1 | docker login --username AWS --password-stdin 775013819650.dkr.ecr.eu-south-1.amazonaws.com
docker buildx build \
  --platform linux/amd64 \
  --progress=auto \
  --tag patty:latest \
  --tag "$IMAGE" \
  --load \
  .
docker push "$IMAGE"

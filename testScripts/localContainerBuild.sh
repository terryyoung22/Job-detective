#!/bin/bash

# This is used for quick local container image build. This whole file can be deleted if you want
# `web` is just what i called the container, you can change the name to anything

# Stopping old image if there is one, removing it, and the image so new can be built
docker stop web
docker rm web
docker rmi web

# Building and running image
docker build -t web ..
docker run -dit --name web web

# Execute bash on build, remove bash for test
docker exec -it web bash
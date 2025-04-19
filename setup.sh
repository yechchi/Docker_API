#!/bin/bash

# Pull API image
docker pull datascientest/fastapi:1.0.0

# Build test images
docker-compose build

# Run tests
docker-compose up

# Cleanup
docker-compose down
#!/bin/bash

set -e

cd front
docker build . -t satellogic_react
cd ../ground
docker build . -t satellogic_core
cd ../tools
docker build . -t satellogic_tools
cd ..
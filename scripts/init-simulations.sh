#!/bin/bash

echo "Deploying Maven proyect..."
scripts/mvn-deploy.sh

cat cases?*.csv > cases.csv
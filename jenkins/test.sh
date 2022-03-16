#!/bin/bash

echo "Test stage"

# Create and activate venv
python3 -m venv venv
source venv/bin/activate

#Install pip requirements
pip3 install -r requirements.txt

# Run pytest
python3 -m pytest --cov=application --cov-report term-missing

#Remove venv
deactivate
rm -rf venv
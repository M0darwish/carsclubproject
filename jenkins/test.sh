#!/bin/bash

echo "Test stage"

# Create and activate venv
python3 -m venv venv
source venv/bin/activate

#Install pip requirements
pip3 install -r requirements.txt

#export env variables 
export SECRET_KEY=$SECRET_KEY
export DATABASE_URI=$TESTING_DATABSE_URI

# Run pytest
python3 -m pytest --cov=application --cov-report term-missing

#Remove venv
deactivate
rm -rf venv
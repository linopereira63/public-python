#!/bin/sh

export FLASK_APP=./service/index.py

# Modified for Windows git bash
#source $(pipenv --venv)/bin/activate
source `pipenv --venv`/Scripts/activate

# flask run -h 0.0.0.0
flask run


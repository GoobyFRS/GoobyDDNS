#!/bin/bash

# Into Repo folder...
cd /your/desired/directory/

# Activate the virtual environment
source venv/bin/activate

# Run the Python script and log output.
/usr/bin/python3 app.py >> ddns_update.log 2>&1

deactivate
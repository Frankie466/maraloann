#!/bin/bash

# Install Python if missing (Optional, depends on environment)
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found! Installing..."
    sudo apt update && sudo apt install python3 -y
fi

if ! command -v pip &> /dev/null
then
    echo "Pip not found! Installing..."
    sudo apt install python3-pip -y
fi

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Run database migrations
python3 manage.py migrate

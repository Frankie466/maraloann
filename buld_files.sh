#!/bin/bash

# Install dependencies
python3 -m pip install --upgrade pip  # Ensure latest pip
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Run migrations
python3 manage.py migrate

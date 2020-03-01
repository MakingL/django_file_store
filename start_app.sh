#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
gunicorn --timeout=20 --workers=1 --bind :9019 file_store.wsgi:application

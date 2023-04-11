#!/bin/bash
source venv/bin/activate
python3 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
gunicorn -b 127.0.0.1:8080 config.wsgi
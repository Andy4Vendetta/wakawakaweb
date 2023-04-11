#!/bin/bash
source venv/Source/activate
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
gunicorn -b 127.0.0.1:8080 config.wsgi
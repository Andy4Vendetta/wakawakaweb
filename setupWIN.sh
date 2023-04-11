#!/bin/bash
python -m venv venv
source venv/Source/activate
pip install -r requirements.txt
echo DEBUG=True >> .env
ABOB=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
echo SECRET_KEY=$ABOB >> .env
echo ALLOWED_HOSTS=localhost,127.0.0.1,79.137.207.11,109.195.147.68 >> .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
gunicorn -b 127.0.0.1:8080 config.wsgi
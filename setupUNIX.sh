#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo DEBUG=True >> .env
ABOB=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
echo SECRET_KEY=$ABOB >> .env
echo ALLOWED_HOSTS=localhost,127.0.0.1,79.137.207.11,109.195.147.68 >> .env
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
gunicorn -b 127.0.0.1:8080 config.wsgi
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo DEBUG=True >> .env
ABOB=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
echo SECRET_KEY=$ABOB >> .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
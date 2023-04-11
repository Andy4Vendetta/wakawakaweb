#!/bin/bash
source venv/Scripts/activate
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
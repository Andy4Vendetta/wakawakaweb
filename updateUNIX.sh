#!/bin/bash
source venv/bin/activate
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
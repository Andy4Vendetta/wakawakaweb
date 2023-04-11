# Installation
## Setup
You can use `./setupUNIX.sh` to automatically setup venv and download needed libs
## Update
To automatically collect static and make migrations you can use `./updateUNIX.sh` script.
## Manual
### Linux/MacOS (Bash, Zsh, etc.):
```sh
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
```
### Windows (PowerShell, cmd):
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

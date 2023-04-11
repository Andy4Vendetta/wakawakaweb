# Installation
## Setup
You can use `./setupUNIX.sh` to automatically setup venv and download needed libs
## Update
To automatically collect static and make migrations you can use `./updateUNIX.sh` script.
## Manual installation
### Linux/MacOS (Bash, Zsh, etc.):
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo DEBUG=True >> .env
ABOB=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
echo SECRET_KEY=$ABOB >> .env
echo ALLOWED_HOSTS=localhost,127.0.0.1 >> .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
gunicorn -b 127.0.0.1:8080 config.wsgi
```
### Windows (PowerShell, cmd):
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
write DEBUG=True to .env.
copy the output and paste it to .env
.env should look like:
```sh
DEBUG=True
SECRET_KEY=ydtwxqz$-061oq351gj08wy4o1lj44^jlp-ilmj3x*w_!%b5dt
ALLOWED_HOSTS=localhost,127.0.0.1,79.137.207.11,109.195.147.68
```
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## Manual updating
You should be in venv to run these commands (`source venv/bin/activate` for Unix-like systems and `venv\Scripts\activate` for Windows)
To manually collect static and make migrations run:
```
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
```
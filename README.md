# Info
The project was created during participation in the [Hackathon "Code Rocks" 2023](https://vk.com/code_rocks_hack_2023) in the competence "development of a site / web application - a site service for finding service providers" among non-professionals.
The final score **195,3/250.**

**The project involved:**

 - [AlexeiBoch](https://github.com/AlexeiBoch) - BackEnd
 - [GravaTharg](https://github.com/GravaTharg) - DevOps, FrontEnd
 - [M00nKate](https://github.com/M00nKate) - Designer, FrontEnd

The site is currently available via this link - *https://hack.tharg.ru/*
# Setup
You can use `./setupUNIX.sh` (Linux/MacOS) or `./setupWIN.sh` (Windows) to automatically setup venv and download needed libs.
All scripts (even for Windows) are written on bash, so use git-bash interpreter, if you are Windows user.
# Update
To automatically collect static and make migrations you can use `./updateUNIX.sh` (Linux/MacOS) or `./updateWIN.sh` (Windows) script.
# Manual setup
## Linux/MacOS:
```sh
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
```
## Windows:
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
echo DEBUG=True >> .env
ABOB=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
echo SECRET_KEY=$ABOB >> .env
echo ALLOWED_HOSTS=localhost,127.0.0.1,79.137.207.11,109.195.147.68 >> .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
# Manual update
You should be in venv to run these commands (`source venv/bin/activate` for Unix-like systems and `source venv/Scripts/activate` for Windows)
## Linux/MacOS:
To manually collect static, make migrations and start server run:
```sh
python3 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
gunicorn -b 127.0.0.1:8080 config.wsgi
```
## Windows:
```sh
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
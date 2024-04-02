FROM python:3.10
WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN pip install --no-cache-dir -r requirements.txt
RUN ABOB=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
RUN echo SECRET_KEY=$ABOB >> .env
RUN echo ALLOWED_HOSTS=localhost,127.0.0.1 >> .env
COPY . .
RUN python3 manage.py makemigrations && python3 manage.py migrate

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "config.wsgi"]

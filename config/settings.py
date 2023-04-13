import environ
import os

from django.urls import reverse_lazy


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Env
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


# Main settings
SECRET_KEY = env.str('SECRET_KEY', 'e@z(&g-mg(z3ypg@@p)43p+=!%xqc156+z)y2td9wm!=%nnee=')

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
    'django_filters',
    'crispy_forms',
    'crispy_bootstrap4',
    'users',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 
        'OPTIONS': {'min_length':5,}
    },
]


# Internationalization
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images, Fonts)
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


# Auth
AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = reverse_lazy('app:main')

LOGIN_URL = reverse_lazy('users:login')

LOGOUT_REDIRECT_URL = reverse_lazy('app:main')

LOGOUT_URL = reverse_lazy('users:logout')


# Mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'wakawakaweb@gmail.com'
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'wakawakaweb@gmail.com'


# Django-cripy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
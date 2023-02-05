import os
from environs import Env

from django.urls import include, path

env = Env()
env.read_env()

ALLOWED_HOSTS = ["192.168.0.101", "localhost", "127.0.0.1"]

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.getenv('DATABASE_NAME'),
    }
}
INSTALLED_APPS = [
    'datacenter',
    "django.contrib.staticfiles",
    "debug_toolbar",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,

    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

STATIC_URL = "static/"

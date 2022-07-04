
from .base import *
import os
from pathlib import Path


DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bdgessai',
        'USER': 'admin_sai',
        'PASSWORD': get_env_setting('DB_MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'bdoracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'webdepto',
        'USER': 'webcario',
        'PASSWORD': get_env_setting('DB_ORACLE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

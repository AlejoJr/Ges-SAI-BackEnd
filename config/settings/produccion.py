
from .base import *
import os
from pathlib import Path



# ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bdgessai',
        'USER': 'root',
        'PASSWORD': 'd1n4m1kjr',  # get_env_setting('DB_MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'bdoracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'webdepto',
        'USER': 'webcario',
        'PASSWORD': 'w3bc4r10p4t4c0n4',  # get_env_setting('DB_ORACLE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

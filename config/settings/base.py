import os
from os.path import dirname, abspath, basename
from pathlib import Path
from sys import path

import ldap
from django_auth_ldap.config import LDAPSearch

ALLOWED_HOSTS = []

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ADMINS = [
    ('Javier Salavert', 'salavert@dsic.upv.es'),
    ('Alejandro Caicedo', 'ajcaipal@upv.es'),
]

# PATH CONFIGURATION
# ------------------------------------------------------------------------------
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-91pw9mu8#g@a*j@1g2@p2%(uz_()*w^y&c0^7fht(#bqxpo0dy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


"""CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]"""

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_crontab',
    'corsheaders',
    'apps.host',
    'apps.pool',
    'apps.sai',
    'apps.user',
    'apps.virtual_machine',
    'apps.group',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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
        'DIRS': [BASE_DIR / 'templates']
        ,
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
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.User'

########################################################################################################################
# LDAP Authentication Settings
########################################################################################################################

"""LDAP_SERVER = 'upvnet.upv.es'
AUTH_LDAP_SERVER_URI = 'ldaps://' + LDAP_SERVER
AUTH_LDAP_BIND_DN = 'agregar'
AUTH_LDAP_BIND_PASSWORD = 'agregar'
AUTH_LDAP_USER_SEARCH = LDAPSearch('dc=upvnet,dc=upv,dc=es', ldap.SCOPE_SUBTREE, '(cn=%(user)s)')
AUTH_LDAP_DN = 'dc=upvnet,dc=upv,dc=es'

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail'
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
)

AUTH_LDAP_GLOBAL_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: False,
    ldap.OPT_REFERRALS: False,
}
"""
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'PAGE_SIZE': 100,  # <-- Desactivar la paginacion cambie a ('PAGE_SIZE': None)
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', # //-> Autenticación por token <-//
        'rest_framework.authentication.SessionAuthentication',# //-> Autenticación por sessión <-//
        #'rest_framework.authentication.BasicAuthentication',
    ]
}

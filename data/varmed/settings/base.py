"""
Django settings for varmed project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

Quick-start development settings - unsuitable for production:
See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
"""

import os

# Where this file itself is located:
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the root directory (where /varapp and /varmed lie)
ROOT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '../../'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'K6QKN6C2xtcl.'  # the one salt that makes 'admin' crypted into 'K6QKN6C2xtcl.' as well.

# SECURITY WARNING: don't run with debug turned on in production!
# (as it will print settings for everybody, including the secret key)
DEBUG = True


# CORS
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
CORS_ALLOW_METHODS = ('GET','POST','PUT','PATCH','DELETE','OPTIONS') # default
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ('x-requested-with','content-type','accept','origin','authorization','x-csrftoken')
CORS_ORIGIN_WHITELIST = (
    'varapp.vital-it.ch',
    'varapp-dev.vital-it.ch'
)
# etc., see https://github.com/ottoyiu/django-cors-headers


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'varapp',
    'mod_wsgi.server',   # run with Apache
    'corsheaders',       # CORS headers
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',  # no need with JWT
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',         # CORS headers
    'django.middleware.common.CommonMiddleware',     # CORS headers
)

ROOT_URLCONF = 'varmed.urls'

# Warning: these caches pickle the data before writing them
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'some-unique-name',
    },
    'genotypes_service': {
        'BACKEND': 'varapp.common.cache.locmem_cache.LocMemNoPickleCache',
        'LOCATION': 'genotypes_service',
    },
    'gene_summary': {
        'BACKEND': 'varapp.common.cache.locmem_cache.LocMemNoPickleCache',
        'LOCATION': 'gene_summary',
    },

    ## Redis
    'redis': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

# Templates: unused, but warns if not defined
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(ROOT_DIR, 'templates')],
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

WSGI_APPLICATION = 'varmed.wsgi.application'


# Databases
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Overwritten in local.py, prod.py etc.
DB_TEST = 'testdb_0036.db'
GEMINI_DB_PATH = '???'     # directory under which gemini databases are stored
DATABASES = {
    'default': {},
}

DATABASE_ROUTERS = ['varapp.routers.AuthRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = False  # Set to False if MySQL with TIMESTAMP fields (https://docs.djangoproject.com/en/1.8/ref/databases/#timestamp-columns)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = ''
STATIC_URL = '/static/'

# Email
EMAIL_ADMIN = 'julien.delafontaine@isb-sib.ch'
EMAIL_FROM = 'varapp@varapp.vital-it.ch'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
#EMAIL_HOST_USER
#EMAIL_HOST_PASSWORD
#EMAIL_USE_TLS
#EMAIL_USE_SSL
#EMAIL_TIMEOUT
#EMAIL_SSL_KEYFILE
#EMAIL_SSL_CERTFILE

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = '/tmp/app-messages' # change this to a proper location

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'debug': {
            'format': "[%(name)s.%(funcName)s] :: %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'debug',
        },
    },
    'loggers': {
        'django': {                # unhandled logs are redirected to this one
            'handlers': ['default'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {    # db queries
            'handlers': ['null'],
            'level': 'ERROR',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'varapp': {    # All varapp.something-named loggers use this one
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}
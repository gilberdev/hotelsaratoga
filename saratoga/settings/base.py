"""
Project main settings file. These settings are common to the project
if you need to override something do it in local.pt
"""

from sys import path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

## PATHS
# Path containing the django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path.append(BASE_DIR)

# Path of the top level directory.
# This directory contains the django project, apps, libs, etc...
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Add apps and libs to the PROJECT_ROOT
path.append(os.path.join(PROJECT_ROOT, "apps"))
path.append(os.path.join(PROJECT_ROOT, "libs"))


## SITE SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/1.8/ref/settings/#installed-apps
INSTALLED_APPS = [

    # 'flat',  # django-flat-theme must be BEFORE contrib.admin


    # Django apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.staticfiles',

    # Third party apps
    'compressor',

    # Local apps
    'base',
]

# https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#using-bcrypt-with-django
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

## DEBUG SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/1.8/ref/settings/#internal-ips
INTERNAL_IPS = ('127.0.0.1')

## LOCALE SETTINGS
# Local time zone for this installation.
# https://docs.djangoproject.com/en/1.8/ref/settings/#time-zone
TIME_ZONE = 'America/Havana'

# https://docs.djangoproject.com/en/1.8/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-tz
USE_TZ = True


## MEDIA AND STATIC SETTINGS
# Absolute filesystem path to the directory that will hold user-uploaded files.
# https://docs.djangoproject.com/en/1.8/ref/settings/#media-root
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public/media')

# URL that handles the media served from MEDIA_ROOT. Use a trailing slash.
# https://docs.djangoproject.com/en/1.8/ref/settings/#media-url
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# https://docs.djangoproject.com/en/1.8/ref/settings/#static-root
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public/static')
#STATIC_ROOT = '/home/hotelsaratoga/projects/hotelsaratoga/saratoga/static/'
STATIC_ROOT = '/var/www/hotelsaratoga.com/static/'

# URL prefix for static files.
# https://docs.djangoproject.com/en/1.8/ref/settings/#static-url
STATIC_URL = '/static/'

# Additional locations of static files
# https://docs.djangoproject.com/en/1.8/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

## TEMPLATE SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.media',
                'django.core.context_processors.request',
                'django.core.context_processors.i18n',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]


## URL SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#root-urlconf.
ROOT_URLCONF = 'saratoga.urls'


## MIDDLEWARE SETTINGS
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# LOGGING
# https://docs.djangoproject.com/en/1.8/topics/logging/
LOGGING = {
    'version': 1,
    'loggers': {
        'saratoga': {
            'level': "DEBUG"
        }
    }
}

# CHARSET
FILE_CHARSET = 'utf-8'

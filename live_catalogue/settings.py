"""
Django settings for live_catalogue project.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wov=)+yrn!$p25*v%qr3ixd57lv=1=^)1qw9@ef3q0)3ves2qc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ASSETS_DEBUG = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'live_catalogue.context_processors.settings_context',
            ],
            'loaders': [
                'frame.loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        }
    }
]

ALLOWED_HOSTS = ('localhost', '127.0.0.1')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_assets',
    'widget_tweaks',
    'django_select2',
    'ckeditor',
    'ckeditor_uploader',
    'gunicorn',
    'frame',
    'flis_metadata.common',
    'flis_metadata.client',
    'live_catalogue',
    'notifications',
    'raven.contrib.django.raven_compat',
)

MIDDLEWARE_CLASSES = (
    'frame.middleware.RequestMiddleware',
    'frame.middleware.UserMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'frame.middleware.SeenMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'frame.backends.FrameUserBackend',
)

ROOT_URLCONF = 'live_catalogue.urls'

WSGI_APPLICATION = 'live_catalogue.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Dynamic config
FORCE_SCRIPT_NAME = os.environ.get('FORCE_SCRIPT_NAME', '')
if FORCE_SCRIPT_NAME:
    USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = FORCE_SCRIPT_NAME + '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FRAME_COOKIES = ['__ac', '_ZopeId']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
FROM_EMAIL = 'no-reply@eionet.europa.eu'

# seen
FRAME_SEEN_MODELS = (
    ('live_catalogue.models.Catalogue', 'created_on'),
)

FRAME_SEEN_EXCLUDE = ('/_lastseencount/', )

METADATA_URL = ''

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = (
    '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
    }
}

if 'test' in sys.argv:
    try:
        from test_settings import *
    except ImportError:
        pass
else:
    try:
        from local_settings import *
    except ImportError:
        pass

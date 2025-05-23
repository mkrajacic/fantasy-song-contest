"""
Django settings for fantasysongcontestsite project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib import messages

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-62$x191up2*#r!u@73&7w299*v1b#x=6#sra0$jb(+i77vmv10"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MESSAGE_TAGS = {
    messages.INFO: "text-white bg-primary",
    messages.SUCCESS: "text-white bg-success",
    messages.WARNING: "text-dark bg-warning",
    messages.ERROR: "text-white bg-danger",
}

# Application definition

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    "teams.apps.TeamsConfig",
    "rules.apps.RulesConfig",
    "results.apps.ResultsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'fantasysongcontestsite.middleware.HtmxMessageMiddleware',
]

ROOT_URLCONF = "fantasysongcontestsite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'common/templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "fantasysongcontestsite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql', 
        'NAME'    : os.getenv('DATABASE_NAME'),                 
        'USER'    : os.getenv('DATABASE_USER'),                    
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),              
        'HOST'    : os.getenv('DATABASE_HOST'),               
        'PORT'    : '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "common/static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Keep existing loggers
    'formatters': {
        'custom_format': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'custom_handler': {
            'level': 'DEBUG',  # Set handler level to DEBUG
            'class': 'logging.StreamHandler',
            'formatter': 'custom_format',
        },
    },
    'loggers': {
        'custom_logger': {
            'handlers': ['custom_handler'],
            'level': 'DEBUG',  # Set logger level to DEBUG
            'propagate': False,  # Prevent logs from propagating to other loggers
        },
    },
}

"""
CUSTOM SETTINGS START HERE
"""
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'unauthorized' #where LoginRequiredMixin redirects
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MAXIMUM_TEAMS_PER_USER = 5
MEMBERS_PER_TEAM = 5
MAXIMUM_USABLE_POINTS = 80
TEAMS_READONLY = False
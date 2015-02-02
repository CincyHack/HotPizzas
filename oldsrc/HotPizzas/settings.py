"""
Django settings for HotPizzas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path


BASE_DIR = Path(__file__).ancestor(2)
STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)
TEMPLATE_DIRS = (
    BASE_DIR.child('templates'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$!g0skv4ku_etamv6pxzyk7m_i)2^7$*@pcqwqqs+9mig!&q^2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'core',
    'oauth2_provider',
    'guardian',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = -1

ROOT_URLCONF = 'HotPizzas.urls'

WSGI_APPLICATION = 'HotPizzas.wsgi.application'

# CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True #FIXME
CORS_ORIGIN_WHITELIST = (
    'pepperonio.com',
)

#Session
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_SAVE_EVERY_REQUEST = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hotpizzas',
        'USER': 'hotpizzas',
        'PASSWORD': 'hotpizzas',
        'HOST': 'develop0.clqblfd0mdpm.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = "/"
LOGIN_URL="/login/"


# Set user model
AUTH_USER_MODEL = 'core.HotPizzasUser'


# Oauth2 settings
OAUTH2_PROVIDER = {
    'SCOPES' : {
        'customer' : 'Customer Scope',
        'driver' : 'Driver Scope',
    },
}


# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.UnicodeJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoObjectPermissions',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
}


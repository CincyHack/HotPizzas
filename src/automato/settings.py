"""
Django settings for automato project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
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
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# FIXME: Use different key in prod
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0(94^)wmz-8h9@%b*=9k6#*#h*uqk!u7$9bio@#d)cb#*p^34_'

# FIXME: Add google key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

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
    'oauth2_provider',
    'social.apps.django_app.default',
    'corsheaders',
    'users',
)

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'automato.urls'

WSGI_APPLICATION = 'automato.wsgi.application'

#FIXME: Change cors headers for prod
CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Set user model
AUTH_USER_MODEL = 'users.AutomatoUser'

# Social Auth settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
URL_PATH = '/'
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.debug.debug'
)



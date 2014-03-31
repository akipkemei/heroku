"""
Django settings for hellodjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'udn==vkegqv-w#&mnk)&)0-a1%4ngw24rql6i57)lplk73o7pl'

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
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hellodjango.urls'

WSGI_APPLICATION = 'hellodjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

##DATABASES = {
##    'default': {
##
##        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
##        'NAME': 'postgres',                      # Or path to database file if using sqlite3.
##        'USER': 'postgres',                      # Not used with sqlite3.
##        'PASSWORD': 'ibanana',                  # Not used with sqlite3.
##        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
##        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
##    }
##}
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'd2kq5ve30vlmm8',
    'HOST': 'ec2-54-197-241-79.compute-1.amazonaws.com',
    'PORT': 5432,
    'USER': 'mscxygirncclpr',
    'PASSWORD': 'qrYgG0PRpRDKDMoZ5tnCqOOrMZ',
  }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/	e

STATIC_URL = '/static/'


# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES['default'] =  dj_database_url.config(default ='postgres://mscxygirncclpr:qrYgG0PRpRDKDMoZ5tnCqOOrMZ@ec2-54-197-241-79.compute-1.amazonaws.com:5432/d2kq5ve30vlmm8')
#------


#DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

#------
#DATABASES['default'] =  dj_database_url.config(default ='postgres://localhost')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

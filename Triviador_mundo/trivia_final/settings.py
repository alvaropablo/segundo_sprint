"""
Django settings for trivia_final project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c*5)*7dhnxw68guyh1_*$5+qi5cn8afru$k_cagg05fno^^nwe'

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
    'trivia_final.apps.usuario',
    'trivia_final.apps.principal',
    'bootstrap3',
    'captcha',
    #control de axeso para ajax
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #control de axeso para ajax
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'trivia_final.urls'

WSGI_APPLICATION = 'trivia_final.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trivia',
        'USER': 'root',
        'PASSWORD': '123456789',
        'HOST': '127.0.0.1',
        'PORT':'3305',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(RUTA_PROYECTO,"media")
TEMPLATE_DIRS=(os.path.join(RUTA_PROYECTO,"plantillas"),)
STATICFILES_DIRS=(os.path.join(RUTA_PROYECTO,"static"),)

RECAPTCHA_PRIVATE_KEY = '6LcBUv4SAAAAABX9tacjKMqIp4kZ2Hm5WMlbCSGB'
RECAPTCHA_PUBLIC_KEY = '6LcBUv4SAAAAAJwOUpWO_dZ7bDd9_Kp2E0urMpyI'

#SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = False

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:4000/',
    'http://127.0.0.1:8000/',
    '*',
)
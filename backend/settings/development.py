from .base import *

import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# # Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR , '.env.dev'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')


ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'emmattxportfoliodb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Email Configurations
EMAIL_HOST =env('EMAIL_HOST')
EMAIL_HOST_USER =env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =env('EMAIL_HOST_PASSWORD')
EMAIL_PORT =env('EMAIL_PORT')

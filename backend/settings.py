"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import dj_database_url
import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# load_dotenv()  # loads the configs from .env
load_dotenv(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))


ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(' ')
# ALLOWED_HOSTS = ['.vercel.app', '.now.sh', '127.0.0.1', 'localhost']

# if not DEBUG:
    # CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split(' ')

    # SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', '0').lower() in ['true', 't', '1']
    # if SECURE_SSL_REDIRECT:
    #     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',

    #3rd party app/packages

    #myOwnApps
    'pages',
    'contact',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.app'




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR / "backend/static/"),
   os.path.join(BASE_DIR / "pages/static/"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DATABASES = {
    "default": 
        dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600, engine='django.db.backends.postgresql' ),
}

# if not DEBUG:
#     # Azure blob storage access key and domain endpoint
#     # AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
#     # AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
#     # AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

#     # storage backend for whitenoise
#     # STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

#     # storage backend for azure
#     # STATICFILES_STORAGE = 'backend.azure_storage.AzureStaticStorage'

#     #persistent mediafiles storage with azure storage
#     # DEFAULT_FILE_STORAGE = 'backend.azure_storage.AzureMediaStorage'

#     # staticfiles management for whitenoise
#     # STATIC_URL = '/static/'

#     # staticfiles management for azure storage
#     STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'

#     STATIC_ROOT = os.path.join(BASE_DIR / 'staticfiles/')


#     MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
#     MEDIA_ROOT = os.path.join(BASE_DIR / 'mediafiles/')

#     # database config
    
#     DATABASES = {
#         "default": 
#             dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600, engine='django.db.backends.postgresql' ),
#     }
# else:
#     STATIC_URL = 'static/'

#     MEDIA_URL = 'media/'
#     MEDIA_ROOT = 'media'

#     # database config
#     DATABASES = {
#         "default": 
#             dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600, engine='django.db.backends.mysql' ),
#     }


# Email Configurations
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = os.getenv('EMAIL_PORT')

# HTTPS settings
# SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE')
# CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE')


# HSTS settings
# SECURE_HSTS_SECONDS =
# SECURE_HSTS_PRELOAD =
# SECURE_HSTS_INCLUDE_SUBDOMAINS =


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from .base import *

import os
from dotenv import load_dotenv
# load_dotenv()  # loads the configs from .env
load_dotenv(BASE_DIR / '.env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split(' ')

SECURE_SSL_REDIRECT = \
  os.getenv('SECURE_SSL_REDIRECT', '0').lower() in ['true', 't', '1']
if SECURE_SSL_REDIRECT:
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('DBNAME'),
    'HOST': os.environ.get('DBHOST'),
    'USER': os.environ.get('DBUSER'),
    'PASSWORD': os.environ.get('DBPASS'),
    'PORT': os.environ.get('DBPORT'),
    'OPTIONS': {'sslmode': 'require'},
  }
}

# Email Configurations
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')

# HTTPS settings
# SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE')
# CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE')


# # HSTS settings
# SECURE_HSTS_SECONDS =
# SECURE_HSTS_PRELOAD =
# SECURE_HSTS_INCLUDE_SUBDOMAINS =


# staticfiles management for whitenoise
# STATIC_ROOT = "staticfiles/"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

#persistent storage with azure storage
DEFAULT_FILE_STORAGE = 'backend.azure_storage.AzureMediaStorage'
STATICFILES_STORAGE = 'backend.azure_storage.AzureStaticStorage'

AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles/'

MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles/'

USE_TZ = True
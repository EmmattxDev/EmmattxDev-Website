from .base import *

import environ
import os 

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    # ALLOWED_HOSTS=(list, [])
)


# # Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR , '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]


# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    #
    # The db() method is an alias for db_url().
    'default': env.db(),

    # read os.environ['SQLITE_URL']
    'extra': env.db_url(
        'SQLITE_URL',
        default='sqlite:////tmp/my-tmp-sqlite.db'
    )
}

# Email Configurations
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')


# CACHES = {
#     # Read os.environ['CACHE_URL'] and raises
#     # ImproperlyConfigured exception if not found.
#     #
#     # The cache() method is an alias for cache_url().
#     'default': env.cache(),

#     # read os.environ['REDIS_URL']
#     'redis': env.cache_url('REDIS_URL')
# }

# HTTPS settings
SESSION_COOKIE_SECURE = env('SESSION_COOKIE_SECURE')
CSRF_COOKIE_SECURE = env('CSRF_COOKIE_SECURE')
SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')
if SECURE_SSL_REDIRECT:
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HSTS settings
SECURE_HSTS_SECONDS = env('SECURE_HSTS_SECONDS')
SECURE_HSTS_PRELOAD = env('SECURE_HSTS_PRELOAD')
SECURE_HSTS_INCLUDE_SUBDOMAINS = env('SECURE_HSTS_INCLUDE_SUBDOMAINS')


# staticfiles management for whitenoise
# STATIC_ROOT = "staticfiles/"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

#persistent storage with azure storage
DEFAULT_FILE_STORAGE = 'backend.azure_storage.AzureMediaStorage'
STATICFILES_STORAGE = 'backend.azure_storage.AzureStaticStorage'

AZURE_ACCOUNT_NAME = env('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = env('AZURE_ACCOUNT_KEY')
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
STATIC_ROOT = "staticfiles/"

MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = "mediafiles/"

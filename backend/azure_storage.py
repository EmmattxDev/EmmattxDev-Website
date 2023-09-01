import os
from storages.backends.azure_storage import AzureStorage
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)


# # Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR , '.env'))

class AzureMediaStorage(AzureStorage):
    account_name = env('AZURE_ACCOUNT_NAME')
    account_key = env('AZURE_ACCOUNT_KEY')
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = env('AZURE_ACCOUNT_NAME')
    account_key = env('AZURE_ACCOUNT_KEY')
    azure_container = 'static'
    expiration_secs = None
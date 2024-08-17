# import os
# from storages.backends.azure_storage import AzureStorage
# from dotenv import load_dotenv
# from backend.settings import BASE_DIR
# # load_dotenv()  # loads the configs from .env
# load_dotenv(BASE_DIR / '.env')

# class AzureMediaStorage(AzureStorage):
#     account_name = os.getenv('AZURE_ACCOUNT_NAME')
#     account_key = os.getenv('AZURE_ACCOUNT_KEY')
#     azure_container = 'media'
#     expiration_secs = None


# class AzureStaticStorage(AzureStorage):
#     account_name = os.getenv('AZURE_ACCOUNT_NAME')
#     account_key = os.getenv('AZURE_ACCOUNT_KEY')
#     azure_container = 'static'
#     expiration_secs = None
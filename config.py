import os
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv('ENV')

# Fastapi config
FASTAPI_HOST = os.getenv('FASTAPI_HOST' if not ENV else 'HOST')
FASTAPI_PORT = int(os.getenv('FASTAPI_PORT' if not ENV else 'PORT'))

# META webhook
META_APP_SECRET = os.getenv('META_APP_SECRET')
META_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
META_VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

# For example usage
YELP_API = os.getenv('YELP_API_KEY')
YELP_CLIENT = os.getenv('YELP_CLIENT_ID')
YELP_URL = os.getenv('YELP_URL')

import os
from dotenv import load_dotenv

load_dotenv()

# Fastapi config
FASTAPI_HOST = os.getenv('FASTAPI_HOST')
FASTAPI_PORT = int(os.getenv('FASTAPI_PORT'))

# META webhook
META_API_URL = os.getenv('META_API_URL')
META_APP_SECRET = os.getenv('META_APP_SECRET')
META_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
META_VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

# For example usage
YELP_API = os.getenv('YELP_API_KEY')
YELP_CLIENT = os.getenv('YELP_CLIENT_ID')
YELP_URL = os.getenv('YELP_URL')

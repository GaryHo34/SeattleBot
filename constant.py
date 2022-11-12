import os
from dotenv import load_dotenv

load_dotenv()

# META webhook
META_API_URL = os.getenv('META_API_URL')
META_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
META_VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

# yelp
YELP_API = os.getenv('YELP_API_KEY')
YELP_CLIENT = os.getenv('YELP_CLIENT_ID')
YELP_URL = os.getenv('YELP_URL')

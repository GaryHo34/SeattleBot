import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('META_API_URL')
ACS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

OPEN_WEATHER_API = os.getenv('OPEN_WEATHER_API')

HEADER = {"Content-Type": "application/json"}
ACCESS_TOKEN = {"access_token": ACS_TOKEN}

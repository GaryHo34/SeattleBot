import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('META_API_URL')
ACS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

HEADER = {"Content-Type": "application/json"}
ACCESS_TOKEN = {"access_token": ACS_TOKEN}

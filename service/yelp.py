import requests
import json

from constant import YELP_API, YELP_CLIENT, YELP_URL
from utiltypes import Business


async def getYelpInfo():
    try:
        headers = {'Authorization': 'Bearer {}'.format(YELP_API)}
        search_api_url = YELP_URL
        params = {'term': 'coffee',
                  'location': 'Seattle, Washington',
                  'limit': 10}
        response = requests.get(
            search_api_url, headers=headers, params=params, timeout=5)
        # print(response.url)
        # print(response.status_code)
        data = response.json()
        print(len(data['businesses']))
        res = list()
        for shop in data['businesses']:
            one = Business(name=shop['name'], address=shop['location']['display_address'][0],
                           rating=shop['rating'], rating_count=shop['review_count'])
            res.append(one)
        # print(res)
        return res
    except:
        response.raise_for_status()

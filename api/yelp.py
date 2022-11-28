from service import get
from constant import YELP_API, YELP_URL
from model import BusinessModel


def get_yelp_info(cuisineType: str):

    headers = {'Authorization': 'Bearer {}'.format(YELP_API)}
    search_api_url = YELP_URL
    params = {'term': cuisineType,
              'location': 'Seattle, Washington',
              'limit': 10}
    response = get(
        search_api_url, headers=headers, params=params, timeout=5).json()

    res = list()
    # Error handle if catch response error, get will return None
    if response and response.get('businesses', None):
        for shop in response['businesses']:
            one = BusinessModel(name=shop['name'], address=shop['location']['display_address'][0],
                                rating=shop['rating'], rating_count=shop['review_count'])
            res.append(one)
    return res

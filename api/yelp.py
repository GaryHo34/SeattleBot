from service import get
from constant import YELP_API, YELP_URL
from model import BusinessModel, UserInfo
from Message import MessageBot

cuisineType = ["Coffee", "Brunch", "Japanese",
               "Mexican", "American", "Chinese"]
typeIdx = [str(i+1) for i in range(len(cuisineType))]


def select_yelp_type(user: UserInfo, messageBot: MessageBot):
    types = [str(i+1) + ". " + c for i,
             c in enumerate(cuisineType)]
    msg = f"What do you want to have?\n" + "   ".join(types)
    messageBot.send_quickreply_message(
        user=user, message=msg, options=typeIdx)


def get_yelp_info(idx: int):
    cuisine = cuisineType[int(idx) - 1]
    headers = {'Authorization': 'Bearer {}'.format(YELP_API)}
    search_api_url = YELP_URL
    params = {'term': cuisine,
              'location': 'Seattle, Washington',
              'limit': 10}
    response = get(
        search_api_url, headers=headers, params=params, timeout=5).json()

    resList = []
    # Error handle if catch response error, get will return None
    if response and response.get('businesses', None):
        for shop in response['businesses']:
            one = BusinessModel(name=shop['name'], address=shop['location']['display_address'][0],
                                rating=shop['rating'], rating_count=shop['review_count'])
            resList.append(one)

    # Organize the list as a string
    res = []
    res.append(
        f"This is the top 10 recommended {cuisine} places: \n")
    for i, shop in enumerate(resList):
        curr = f'{i+1}: {shop.name}\n' + \
            f'  address: {shop.address}\n' + \
            f'  rating: {shop.rating}\n' + \
            f'  rating_count: {shop.rating_count}\n'
        res.append(curr)
    res = "".join(res)
    return res


def get_yelp_typeIdx():
    return typeIdx

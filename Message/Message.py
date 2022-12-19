from constant import META_ACCESS_TOKEN
from typing import Optional, List
from model import UserInfo
from service import post
from helper import *

# constant
MESSAGE_PROFILE_URL = "https://graph.facebook.com/v15.0/me/messenger_profile"
HEADER = {"Content-Type": "application/json"}
PARAMS = {"access_token": META_ACCESS_TOKEN}


def set_messenger_profile():
    post(
        url=MESSAGE_PROFILE_URL,
        headers=HEADER,
        params=PARAMS,
        data={
            "get_started": {"payload": "start"},
            "greeting": [
                {
                    "locale": "default",
                    "text": "Hello!This is your Best Seattle Local Guide!",
                }
            ],
            "persistent_menu": [
                generate_menu(buttons=[
                    generate_web_button(
                        title="Our GitHub Page", url="https://github.com/GaryHo34/SeattleBot"),
                    generate_postback_button(
                        title="Local Recommendation", postback="yelp"),
                    generate_postback_button(
                        title="Quick Actions", postback="quick"),
                ])
            ]
        },
    )


class MessageBot():
    def __init__(self):
        set_messenger_profile()

    def send_text_message(self, user: UserInfo, message: str):
        return send_text_message(user, message)

    def send_template_message(self, user: UserInfo, message: str):
        return send_template_message(user, message)

    def send_home_message(self, user: UserInfo):
        return send_home_message(user)

    def send_quickreply_message(self, user: UserInfo, message: str, options: Optional[List[str]] = None):
        return send_quickreply_message(user, message, options)

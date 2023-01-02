from config import META_ACCESS_TOKEN, META_API_URL
from typing import Optional, List, Union
from model import UserInfo, TextMessage, WeburlButton, PostbackButton, QuickReply, QuickReplyMessage, PersistentMenu
from utils import post
from typing import Optional, List, Union

# constant
MESSAGE_PROFILE_URL = "https://graph.facebook.com/v15.0/me/messenger_profile"
PARAMS = {"access_token": META_ACCESS_TOKEN}
IMAGE_SRC = "https://media.cntraveler.com/photos/60480c67ff9cba52f2a91899/16:9/w_2560%2Cc_limit/01-velo-header-seattle-needle.jpg"


def generate_menu(
    buttons: List[Union[PostbackButton, WeburlButton]],
    locale: Optional[str] = None,
    composer_input_disable: Optional[bool] = None
) -> PersistentMenu:
    """
    It generates a persistent menu for the bot.

    Args:
      buttons (List[Union[PostbackButton, WeburlButton]]):
    List[Union[PostbackButton, WeburlButton]]
      locale (Optional[str]): The locale of the menu.
      composer_input_disable (Optional[bool]): This is a boolean value that
    determines whether the user can type in the text field to send a message to the
    bot.

    Returns:
      A dictionary representing persistent menu
    """
    if (locale and composer_input_disable != None):
        PersistentMenu(
            locale=locale, composer_input_disabled=composer_input_disable, buttons=buttons).dict()
    return PersistentMenu(call_to_actions=buttons).dict()


def generate_web_button(title: str, url: str) -> WeburlButton:
    """
    > This function takes in a title and a url and returns a WeburlButton object

    Args:
      title (str): The title of the button.
      url (str): The URL to open when the button is clicked.

    Returns:
      A dictionary representing web url button
    """
    return WeburlButton(title=title, url=url).dict()


def generate_postback_button(title: str, postback: str) -> PostbackButton:
    """
    It takes a title and a postback and returns a postback button

    Args:
      title (str): The title of the button.
      postback (str): The postback string that will be sent to the bot when the
    button is tapped.

    Returns:
      A dictionary representing post back button
    """
    return PostbackButton(title=title, payload=postback).dict()


def generate_quickreply_message(
    message: str,
    options: Optional[List[str]] = None
) -> QuickReplyMessage:
    """
    It takes a message and a list of options, and returns a QuickReplyMessage object

    Args:
      message (str): The message you want to send.
      options (Optional[List[str]]): A list of strings that will be used as the
    quick reply options.

    Returns:
      A dictionary
    """
    optionList: List[QuickReply] = []
    if options:
        for option in options:
            optionList.append(QuickReply(title=option, payload=option))
    return QuickReplyMessage(text=message, quick_replies=optionList).dict()


def send_text_message(user: UserInfo, message: str):
    """
    It sends a text message to the user

    Args:
      user (UserInfo): UserInfo - the user to send the message to
      message (str): The message to send to the user.
    """
    post(
        url=META_API_URL,
        params=PARAMS,
        data={
            "recipient": {"id": user.recipient_id},
            "message": TextMessage(text=message).dict()
        },
    )


def send_quickreply_message(
    user: UserInfo,
    message: str,
    options: Optional[List[str]] = None
):
    """
    It sends a quick reply message to the user

    Args:
      user (UserInfo): UserInfo
      message (str): The message to be sent.
      options (Optional[List[str]]): List of strings that will be used as the quick
    reply options.
    """
    post(
        url=META_API_URL,
        params=PARAMS,
        data={
            "recipient": {"id": user.recipient_id},
            "message": generate_quickreply_message(message, options)
        },
    )


def send_template_message(user: UserInfo, message: str):
    """
    It sends a template message to the user with a button that opens the Messenger
    website and another button that sends a postback payload to the bot

    Args:
      user (UserInfo): UserInfo
      message (str): The message to be sent.
    """
    post(
        url=META_API_URL,
        params=PARAMS,
        data={
            "recipient": {"id": user.recipient_id},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": message,
                        "buttons": [
                            WeburlButton(title="Visit Messenger",
                                         url="https://www.messenger.com").dict(),
                            PostbackButton(title="Ask weather",
                                           payload="weather").dict()
                        ]
                    }
                }
            }
        }
    )


def send_home_message(user: UserInfo):
    """
    This function sends a message to the user with a welcome message and a list of
    buttons that the user can click on

    Args:
      user (UserInfo): UserInfo
    """
    post(
        url=META_API_URL,
        params=PARAMS,
        data={
            "recipient": {
                "id": user.recipient_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                            "template_type": "generic",
                        "elements": [
                            {
                                "title": "Welcome!",
                                "image_url": IMAGE_SRC,
                                "subtitle": "Your BEST Seattle local guide!",
                                "default_action": {
                                            "type": "web_url",
                                            "url": "https://github.com/GaryHo34/SeattleBot",
                                            "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    generate_web_button(
                                        title="Our GitHub Page", url="https://github.com/GaryHo34/SeattleBot"),
                                    generate_postback_button(
                                        title="Local Recommendation", postback="yelp"),
                                    generate_postback_button(
                                        title="Quick Actions", postback="quick"),
                                ]
                            }
                        ]
                    }
                }
            }
        }
    )


def set_messenger_profile():
    """
    It sends a POST request to the Messenger Profile API endpoint with the following
    data:

    - A get_started button with a payload of start
    - A greeting message
    - A persistent menu with a button that opens a webview, a button that triggers a
    postback, and a button that triggers a postback
    """
    post(
        url=MESSAGE_PROFILE_URL,
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


class MessengerBot():
    def __init__(self, set_profile: bool):
        """

        This function is called when the class is instantiated. It takes one argument,
        `set_profile`, which is a boolean. If `set_profile` is `True`, the function
        `set_messenger_profile()` is called

        Args:
          set_profile (bool): If set to True, the Messenger Profile will be set.
        """
        if set_profile:
            set_messenger_profile()

    def send_text_message(self, user: UserInfo, message: str):
        return send_text_message(user, message)

    def send_template_message(self, user: UserInfo, message: str):
        return send_template_message(user, message)

    def send_home_message(self, user: UserInfo):
        return send_home_message(user)

    def send_quickreply_message(self, user: UserInfo, message: str, options: Optional[List[str]] = None):
        return send_quickreply_message(user, message, options)

from constant import META_ACCESS_TOKEN, META_API_URL
from model.MessageModel import TextMessage, WeburlButton, PostbackButton, QuickReply, QuickReplyMessage
from typing import Optional, List
from service import post
from model import UserInfo

# constant
HEADER = {"Content-Type": "application/json"}
PARAMS = {"access_token": META_ACCESS_TOKEN}


def generate_web_button(title: str, url: str) -> WeburlButton:
    return WeburlButton(title, url)


def generate_postback_button(title: str, postback: str) -> PostbackButton:
    return WeburlButton(title, postback)


def generate_quickreply_message(message: str, options: Optional[List[str]] = None) -> QuickReplyMessage:
    optionList: List[QuickReply] = []
    if options:
        for option in options:
            optionList.append(QuickReply(title=option, payload=option))
    return QuickReplyMessage(text=message, quick_replies=optionList)


def send_text_message(user: UserInfo, message: str):
    post(
        url=META_API_URL,
        headers=HEADER,
        params=PARAMS,
        data={
            "recipient": {"id": user.recipient_id},
            "message": TextMessage(text=message).dict()
        },
    )


def send_quickreply_message(user: UserInfo, message: str, options: Optional[List[str]] = None):
    post(
        url=META_API_URL,
        headers=HEADER,
        params=PARAMS,
        data={
            "recipient": {"id": user.recipient_id},
            "message": generate_quickreply_message(message, options).dict()
        },
    )


def send_template_message(user: UserInfo, message: str):
    post(
        url=META_API_URL,
        headers=HEADER,
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
    post(
        url=META_API_URL,
        headers=HEADER,
        params=PARAMS,
        json={
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
                                "image_url": "https://media.cntraveler.com/photos/60480c67ff9cba52f2a91899/16:9/w_2560%2Cc_limit/01-velo-header-seattle-needle.jpg",
                                "subtitle": "Your BEST Seattle local guide!",
                                "default_action": {
                                            "type": "web_url",
                                            "url": "https://github.com/GaryHo34/SeattleBot",
                                            "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                                "url": "https://github.com/GaryHo34/SeattleBot",
                                                "title": "Our GitHub Page"
                                    }, {
                                        "type": "postback",
                                                "title": "Start Chatting",
                                                "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }
    )
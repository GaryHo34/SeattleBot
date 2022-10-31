from schemas import *
from constant import *
from utiltypes import UserInfo
from utils import *
import httpx


async def send_text_message(user: UserInfo, message: str):
    try:
        response = httpx.post(
            url=API_URL,
            params=ACCESS_TOKEN,
            headers=HEADER,
            json={
                "recipient": {"id": user.recipient_id},
                "message": generateTextMessage(message)
            },
        )
    except:
        # This is an http error
        response.raise_for_status()


async def send_QuickReply_message(user: UserInfo, message: str):
    try:
        response = httpx.post(
            url=API_URL,
            params=ACCESS_TOKEN,
            headers=HEADER,
            json={
                "recipient": {"id": user.recipient_id},
                "message": generateQuickReplyMessage(message)
            },
        )
    except:
        # This is an http error
        response.raise_for_status()


async def send_template_message(user: UserInfo):
    try:
        response = httpx.post(
            url=API_URL,
            params=ACCESS_TOKEN,
            headers=HEADER,
            json={
                "recipient": {"id": user.recipient_id},
                "message": {
                    "attachment": {
                        "type": "template",
                        "payload": generateButtonMessage("What do you want to do next?")
                    }
                }
            }
        )
    except:
        # This is an http error
        response.raise_for_status()


async def send_home_message(user: UserInfo):
    try:
        home_response = httpx.post(
            url=user.url,
            params={"access_token": user.page_access_token},
            headers={"Content-Type": "application/json"},
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
    except:
        # This is an http error
        home_response.raise_for_status()

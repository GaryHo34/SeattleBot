from schemas.schema import UserInfo
import httpx


async def send_message(user: UserInfo):
    try:
        response = httpx.post(
            url=url,
            params={"access_token": user.page_access_token},
            headers={"Content-Type": "application/json"},
            json={
                "recipient": {"id": user.recipient_id},
                "message": {"text": user.message_text},
                "messaging_type": user.message_type,
            },
        )
    except:
        # This is an http error
        response.raise_for_status()


async def send_button_message(user: UserInfo):
    try:
        response = httpx.post(
            url=user.url,
            params={"access_token": user.page_access_token},
            headers={"Content-Type": "application/json"},
            json={
                "recipient": {"id": user.recipient_id},
                "message": {
                    "text": "What do you want to know?",
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "Weather",
                            "payload": "I want to know weather"
                        }, {
                            "content_type": "text",
                            "title": "temperature",
                            "payload": "I want to know temperature"
                        }
                    ]
                },
                "messaging_type": user.message_type,
            },
        )
    except:
        # This is an http error
        response.raise_for_status()


async def send_next_message(user: UserInfo):
    try:
        response = httpx.post(
            url=user.url,
            params={"access_token": user.page_access_token},
            headers={"Content-Type": "application/json"},
            json={
                "recipient": {"id": user.recipient_id},
                "message": {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "button",
                            "text": "What do you want to do next?",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": "https://www.messenger.com",
                                    "title": "Visit Messenger"
                                },
                                {
                                    "type": "web_url",
                                    "url": "https://www.youtube.com",
                                    "title": "Visit Youtube"
                                },
                            ]
                        }
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

from utiltypes import *


def generateOption(title: str, payload: str, image_url=""):
    return {
        "content_type": "text",
        "title": title,
        "payload": payload,
        "image_url": image_url
    }


def generateGenericMessage():
    return {
        "template_type": TEMPLATE_TYPE.GENERIC,
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

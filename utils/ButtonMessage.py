from utiltypes import *


def generateButton(type: str, title: str, url="", payload=""):
    if type == BUTTON_TYPE.URL:
        return {
            "type": type,
            "url": url,
            "title": title,
        }
    else:
        return {
            "type": type,
            "title": title,
            "payload": payload,
        }


def generateButtonMessage(message: str):
    return {
        "template_type": TEMPLATE_TYPE.BUTTON,
        RESPONSE_TYPE.TEXT: message,
        RESPONSE_TYPE.BUTTONS: [
            generateButton(BUTTON_TYPE.URL, "Visit Messenger",
                           "https://www.messenger.com", ""),
            generateButton(BUTTON_TYPE.POSTBACK, "Visit Messenger",
                           "", "Messenger"),
        ]
    }

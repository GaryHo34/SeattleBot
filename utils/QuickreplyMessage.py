from utiltypes import *


def generateOption(title: str, payload: str, image_url=""):
    return {
        "content_type": "text",
        "title": title,
        "payload": payload,
        "image_url": image_url
    }


def generateQuickReplyMessage(message: str, *arg):
    return {
        RESPONSE_TYPE.TEXT: message,
        RESPONSE_TYPE.QUICK_REPLIES: [
            generateOption("weather", "the weather info"),
            generateOption("temprature", "the temparature info")
        ]
    }

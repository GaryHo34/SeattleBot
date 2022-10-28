from pydantic import BaseModel
from typing import List
import uvicorn
import httpx
from fastapi import FastAPI, Request, Response
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

API_URL = os.getenv('META_API_URL')
ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')


class WebhookRequestData(BaseModel):
    object: str = ""
    entry: List = []

# Helpers


async def send_message(
    url: str,
    page_access_token: str,
    recipient_id: str,
    message_text: str,
    message_type: str = "UPDATE",
):
    try:
        response = httpx.post(
            url=url,
            params={"access_token": page_access_token},
            headers={"Content-Type": "application/json"},
            json={
                "recipient": {"id": recipient_id},
                "message": {"text": message_text},
                "messaging_type": message_type,
            },
        )
    except:
        # This is an http error
        response.raise_for_status()

# Helpers


async def send_button_message(
    url: str,
    page_access_token: str,
    recipient_id: str,
    message_type: str = "RESPONSE",
):
    try:
        response = httpx.post(
            url=url,
            params={"access_token": page_access_token},
            headers={"Content-Type": "application/json"},
            json={
                "recipient": {"id": recipient_id},
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
                "messaging_type": message_type,
            },
        )
    except:
        # This is an http error
        response.raise_for_status()


async def send_next_message(
    url: str,
    page_access_token: str,
    recipient_id: str,
    message_type: str = "RESPONSE",
):
    try:
        response = httpx.post(
            url=url,
            params={"access_token": page_access_token},
            headers={"Content-Type": "application/json"},
            json={
                "recipient": {"id": recipient_id},
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


async def send_home_message(
    url: str,
    page_access_token: str,
    recipient_id: str,
    message_type: str = "RESPONSE",
):
    try:
        home_response = httpx.post(
            url=url,
            params={"access_token": page_access_token},
            headers={"Content-Type": "application/json"},
            json={
                "recipient": {
                    "id": recipient_id
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


@ app.get("/")
def fb_webhook(request: Request):
    if (request.query_params.get("hub.mode") == "subscribe" and
            request.query_params.get("hub.challenge")):
        if (request.query_params.get("hub.verify_token") != VERIFY_TOKEN):
            return Response(content="Verification token mismatch", status_code=403)
        return Response(content=request.query_params["hub.challenge"])
    return Response(content="Required arguments haven't passed.", status_code=400)


@ app.post("/")
async def webhook(data: WebhookRequestData):
    """
    Messages handler.
    """
    # print(data)
    if data.object == "page":
        for entry in data.entry:
            messaging_events = [
                event for event in entry.get("messaging", []) if event.get("message")
            ]
            for event in messaging_events:
                message = event.get("message")
                sender_id = event["sender"]["id"]

                if message['text'] == "weather":
                    await send_button_message(url=API_URL,
                                              page_access_token=ACCESS_TOKEN,
                                              recipient_id=sender_id)
                elif message['text'] == "next":
                    await send_next_message(url=API_URL,
                                            page_access_token=ACCESS_TOKEN,
                                            recipient_id=sender_id)
                else:
                    await send_home_message(url=API_URL,
                                            page_access_token=ACCESS_TOKEN,
                                            recipient_id=sender_id)

    print("PK")
    return Response(content="ok")


# Debug.
def main():
    if VERIFY_TOKEN:
        print("your verify token is: ", VERIFY_TOKEN)
    uvicorn.run(app=app)


if __name__ == "__main__":
    main()

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
                            "title": "temparaturre",
                            "payload": "I want to know temparaturre"
                        }
                    ]
                },
                "messaging_type": message_type,
            },
        )
    except:
        # This is an http error
        response.raise_for_status()


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
    print(data)
    if data.object == "page":
        for entry in data.entry:
            messaging_events = [
                event for event in entry.get("messaging", []) if event.get("message")
            ]
            for event in messaging_events:
                message = event.get("message")
                sender_id = event["sender"]["id"]

                await send_button_message(url=API_URL,
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

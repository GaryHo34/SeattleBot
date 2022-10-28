from pydantic import BaseModel
from typing import List
import uvicorn
import httpx
from fastapi import FastAPI, Request, Response
from dotenv import load_dotenv
import os
from schemas.helper import *
from schemas.schema import WebhookRequestData, UserInfo

app = FastAPI()
load_dotenv()

API_URL = os.getenv('META_API_URL')
ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

# Helpers


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

                user = UserInfo(url=API_URL,
                                page_access_token=ACCESS_TOKEN,
                                recipient_id=sender_id)

                if message['text'] == "weather":
                    await send_button_message(user)
                elif message['text'] == "next":
                    await send_next_message(user)
                else:
                    await send_home_message(user)

    print("PK")
    return Response(content="ok")


# Debug.
def main():
    if VERIFY_TOKEN:
        print("your verify token is: ", VERIFY_TOKEN)
    uvicorn.run(app=app)


if __name__ == "__main__":
    main()

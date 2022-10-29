from typing import List
import uvicorn
from fastapi import FastAPI, Request, Response
from constant import *
from schemas import *
from utiltypes import *

app = FastAPI()

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
                                page_access_token=ACCESS_TOKEN["access_token"],
                                recipient_id=sender_id)
                await send_QuickReply_message(user, "what do you want to know today?")
                # to-do seperate function to function..
                if message['text'] == "weather":
                    await send_template_message(user)
                elif message['text'] == "next":
                    await send_template_message(user)
                else:
                    await send_home_message(user)
    return Response(content="ok")

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,
                reload=True)

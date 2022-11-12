from fastapi import FastAPI, Request, Response
import uvicorn
from typing import List
from model import UserInfo, WebhookRequestData
from helper import send_template_message, send_text_message, send_quickreply_message
from api import getWeatherInfo, getYelpInfo
from constant import META_VERIFY_TOKEN

app = FastAPI()

# Helpers


@app.get("/")
def fb_webhook(request: Request):
    if (request.query_params.get("hub.mode") == "subscribe" and
            request.query_params.get("hub.challenge")):
        if (request.query_params.get("hub.verify_token") != META_VERIFY_TOKEN):
            return Response(content="Verification token mismatch", status_code=403)
        return Response(content=request.query_params["hub.challenge"])
    return Response(content="Required arguments haven't passed.", status_code=400)


@app.post("/")
def webhook(data: WebhookRequestData):
    """
    Messages handler.
    """
    # print(data)
    if data.object == "page":
        for entry in data.entry:
            messaging_events = [
                event for event in entry.get("messaging", []) if event.get("message") or event.get("postback")
            ]

            for event in messaging_events:
                postback = event.get("postback", None)
                message = event.get("message", None)
                sender_id = event["sender"]["id"]

                user = UserInfo(recipient_id=sender_id)

                if message and message.get('text', '') == "yelp":
                    resList = getYelpInfo()
                    res = []
                    res.append(
                        "This is the top 10 recommended coffee places: \n")
                    for i, shop in enumerate(resList):
                        curr = f'{i+1}: {shop.name}\n  address: {shop.address}\n  rating: {shop.rating},\n  rating_count: {shop.rating_count}\n'
                        res.append(curr)
                    res = "".join(res)
                    send_text_message(user, res)
                    return

                if message.get('quick_reply', None) and message['quick_reply'].get('payload', None)== "weather":
                    temp, weather = getWeatherInfo()
                    send_text_message(
                        user, f'The temprature is {temp}F, the weather is {weather}')
                    return

                send_quickreply_message(
                    user, "What do you want to know", ["weather", "yelp"])

    return Response(content="ok")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

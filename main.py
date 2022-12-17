from fastapi import FastAPI, Request, Response
import uvicorn
from typing import List
from model import UserInfo, WebhookRequestData
from helper import *
from api import get_weather_info, get_yelp_info
from constant import META_VERIFY_TOKEN
from Message import MessageBot

app = FastAPI()

messageBot = MessageBot()
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
    print(data)
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
                # Types of restaurants
                cuisineType = ["Coffee", "Brunch", "Japanese",
                               "Mexican", "American", "Chinese"]
                typeIdx = [str(i+1) for i in range(len(cuisineType))]

                if postback and postback.get('payload', None) == "start":
                    messageBot.send_home_message(user)

                if (message and message.get('text', '') == "yelp") or (postback and postback.get('payload', None) and postback['payload'] == "yelp"):
                    types = [str(i+1) + ". " + c for i,
                             c in enumerate(cuisineType)]
                    msg = f"What do you want to have?\n" + "   ".join(types)
                    messageBot.send_quickreply_message(user, msg, typeIdx)
                    return

                if message and message.get('quick_reply', None) and message['quick_reply'].get('payload', None) in typeIdx:
                    idx = message['quick_reply'].get('payload', None)
                    cuisine = cuisineType[int(idx) - 1]
                    resList = get_yelp_info(cuisine)
                    res = []
                    res.append(
                        f"This is the top 10 recommended {cuisine} places: \n")
                    for i, shop in enumerate(resList):
                        curr = f'{i+1}: {shop.name}\n' + \
                            f'  address: {shop.address}\n' + \
                            f'  rating: {shop.rating}\n' + \
                            f'  rating_count: {shop.rating_count}\n'
                        res.append(curr)
                    res = "".join(res)
                    messageBot.send_text_message(user, res)
                    return

                if message and message.get('quick_reply', None) and message['quick_reply'].get('payload', None) == "weather":
                    temp, weather = get_weather_info()
                    messageBot.send_text_message(
                        user, f'The temprature is {temp}F, the weather is {weather}')
                    return

                if postback and postback.get('payload', None) and postback['payload'] == "quick":
                    messageBot.send_quickreply_message(
                        user, "What do you want to know", ["weather", "yelp"])
                    return

    return Response(content="ok")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

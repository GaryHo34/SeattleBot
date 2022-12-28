import uvicorn
from fastapi import FastAPI, Request, Response
from config import META_VERIFY_TOKEN, FASTAPI_HOST, FASTAPI_PORT
from model import UserInfo, WebhookRequestData
from api import get_weather_info, get_yelp_info, select_yelp_type, get_yelp_typeIdx
from utils import event_parser
from messenger import MessengerBot

app = FastAPI()
messageBot = MessengerBot(set_profile=False)


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
    if data.object != "page" or not data.entry:
        return Response(content="Incorrect webhook", status_code=401)

    for entry in data.entry:
        if not entry.get("messaging"):
            return Response(content="Message not found", status_code=401)

    messaging_events = list(map(event_parser, entry.get("messaging")))

    for event in messaging_events:
        user = UserInfo(recipient_id=event.sender)

        if event.payload == "start":
            messageBot.send_home_message(user)

        if event.text == "yelp" or event.payload == "yelp":
            select_yelp_type(user, messageBot)
            return Response(content="ok")

        if event.quick_reply in get_yelp_typeIdx():
            res = get_yelp_info(int(event.quick_reply))
            messageBot.send_text_message(user, res)
            return Response(content="ok")

        if event.quick_reply == "weather":
            temp, weather = get_weather_info()
            messageBot.send_text_message(
                user, f'The temprature is {temp}F, the weather is {weather}')
            return Response(content="ok")

        if event.payload == "quick":
            messageBot.send_quickreply_message(
                user=user, message="What do you want to know", options=["weather", "yelp"])
            return Response(content="ok")
        
        else:
            messageBot.send_home_message(user)

    return Response(content="ok")


if __name__ == "__main__":
    uvicorn.run("main:app", host=FASTAPI_HOST, port=FASTAPI_PORT, reload=True)

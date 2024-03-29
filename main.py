import uvicorn
from fastapi import FastAPI, Response, Depends, Query
from config import META_VERIFY_TOKEN, FASTAPI_HOST, FASTAPI_PORT
from model import Event
from example.api import get_weather_info, get_yelp_info, select_yelp_type, get_yelp_typeIdx
from utils import event_parser, verify_payload
from typing import List
from messenger import MessengerBot

app = FastAPI()
messageBot = MessengerBot(set_profile=True)


@app.get("/")
def verify_webhook(
    hub_mode: str = Query(alias="hub.mode"),
    hub_challenge: str = Query(alias="hub.challenge"),
    hub_verify_token: str = Query(alias="hub.verify_token"),
):
    """
    This route is only for webhook address validation.
    """
    if hub_mode != "subscribe" or not hub_challenge:
        return Response(content="Unrecognized params", status_code=400)
    if hub_verify_token != META_VERIFY_TOKEN:
        return Response(content="Verification token mismatch", status_code=403)
    return Response(content=hub_challenge)


@app.post("/", dependencies=[Depends(verify_payload)])
def message_webhook(events: List[Event] = Depends(event_parser)):
    """
    It receives a list of events from the webhook, and then for each event, it
    checks if the event is a text message, and if so, it sends a corresponding
    response back to the user

    Args:
      events (List[Event]): List[Event] = Depends(event_parser)

    Returns:
      a response object with the content "ok"
    """
    if not events:
        return Response(content="Unrecognized webhook", status_code=401)

    for event in events:
        if event.text.find("echo") == 0:
            words = event.text.split(' ')
            messageBot.send_text_message(
                recipient_id=event.sender,
                message=' '.join(words[1:]),
            )
            return Response(content="ok")

        if event.payload == "start":
            messageBot.send_text_message(
                recipient_id=event.sender,
                message="Hello, world!",
            )
            return Response(content="ok")

        if event.quick_reply == "echo":
            temp, weather = get_weather_info()
            messageBot.send_text_message(
                recipient_id=event.sender,
                message="Type echo <YOUR MESSAGE>"
            )
            return Response(content="ok")

        if event.quick_reply == "weather":
            temp, weather = get_weather_info()
            messageBot.send_text_message(
                recipient_id=event.sender,
                message=f'The temprature is {temp}F, the weather is {weather}'
            )
            return Response(content="ok")

        if event.payload == "quick":
            messageBot.send_quickreply_message(
                recipient_id=event.sender,
                message="This is a quick message example",
                options=["echo", "weather"]
            )
            return Response(content="ok")

        else:
            messageBot.send_home_message(recipient_id=event.sender)

    return Response(content="ok")


if __name__ == "__main__":
    uvicorn.run("main:app", host=FASTAPI_HOST, port=FASTAPI_PORT, reload=True)

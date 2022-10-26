import requests
from fastapi import FastAPI, Request, Response
from dotenv import load_dotenv
import json
import os

app = FastAPI()
load_dotenv()

API = "https://graph.facebook.com/v15.0/me/messages?access_token=" + \
    os.getenv('PAGE_ACCESS_TOKEN')


def fb_send_message(to, message):
    message = json.dumps({
        "recipient": {"id": to},
        "message": {"text": message}
    })

    req = requests.post(API,
                        headers={"Content-Type": "application/json"},
                        data=message)
    print(req.status_code)


@app.get("/api/webhook")
def fb_webhook(request: Request):
    if request.query_params.get("hub.mode") == "subscribe" and request.query_params.get(
        "hub.challenge"
    ):
        if (
            not request.query_params.get("hub.verify_token")
            == os.getenv('VERIFY_TOKEN')
        ):
            return Response(content="Verification token mismatch", status_code=403)
        return Response(content=request.query_params["hub.challenge"])
    return Response(content="Required arguments haven't passed.", status_code=400)


@app.post("/api/webhook")
async def fb_receive_message(request: Request):
    data = await request.body()
    message_entries = json.loads(data.decode('utf8'))['entry']
    for entry in message_entries:
        for message in entry['messaging']:
            id = message['sender']['id']
            text = message['message']['text']
            print("{} says {}".format(id, text))
            fb_send_message(id, message="echo>>"+text)
    return Response(content="Recived webhook", status_code=200)

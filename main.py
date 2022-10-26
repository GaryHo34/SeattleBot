from fastapi import FastAPI, Request, Response
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

API = "https://graph.facebook.com/v15.0/me/messages?access_token="+os.getenv('PAGE_ACCESS_TOKEN')

@app.get("/api/webhook")
def fbverify(request: Request):
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
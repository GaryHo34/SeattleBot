from fastapi import FastAPI, Request, Response
import os

app = FastAPI()

PAGE_ACCESS_TOKEN = "EAAG4nCYakrABAP0b8wZCdSxftpoWZCsPVaRu6KtguEBvtILnosYHYGJjoiMHrELZBsClHE0sVdWUpedM1Rto6tTHk2qZCEvTMlfVINqm0MWGCbOZBM28Q2dXZCeahDa8bFXGrnI6dDc8QRpqTKZCpEHLjh9kwctKVjrQFx5EZCRbHy8nklO6MfPZATUqixZBaAnMkZC2ZAZAKjVmOegZDZD"
api = "https://graph.facebook.com/v15.0/me/messages?access_token="+PAGE_ACCESS_TOKEN

@app.get("/")
def fbverify(request: Request):
    if request.query_params.get("hub.mode") == "subscribe" and request.query_params.get(
        "hub.challenge"
    ):
        if (
            not request.query_params.get("hub.verify_token")
            == "YOUR_VERIFY_TOKEN"
        ):
            return Response(content="Verification token mismatch", status_code=403)
        return Response(content=request.query_params["hub.challenge"])

    return Response(content="Required arguments haven't passed.", status_code=400)


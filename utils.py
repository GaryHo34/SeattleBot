import requests
from fastapi import Header, Request, Response
from config import META_APP_SECRET
from model import Event, WebhookRequestData
from typing import Optional, List
import hmac


def get(
    url: str,
    headers: Optional[dict] = None,
    params: Optional[dict] = None,
    timeout: Optional[int] = None,
):
    try:
        response = requests.get(url=url,
                                headers=headers,
                                params=params,
                                timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    return None


def post(
    url: str,
    data: dict,
    headers: Optional[dict] = {"Content-Type": "application/json"},
    params: Optional[dict] = None
):
    try:
        response = requests.post(url=url,
                                 headers=headers,
                                 params=params,
                                 json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    return None


async def verify_payload(request: Request, X_Hub_Signature_256: str = Header()):
    data = await request.body()
    expectedHash = hmac.new(
        META_APP_SECRET.encode(), data, "sha256").hexdigest()
    if expectedHash != X_Hub_Signature_256[7:]:
        return Response(content="Couldn't validate the request signature.", status_code=401)


def get_event(event):
    postback = event.get("postback")
    message = event.get("message")
    quick_rp = message.get('quick_reply') if message else None
    sender_id = event["sender"]["id"]

    return Event(
        type='message' if message else 'postback' if postback else '',
        sender=sender_id,
        text=message.get('text') if message else '',
        quick_reply=quick_rp.get('payload') if quick_rp else '',
        payload=postback.get('payload') if postback else '',
    )


def event_parser(data: WebhookRequestData) -> List[Event]:
    if data.object != "page" or not data.entry:
        return []

    if not data.entry[0].get("messaging"):
        return []

    return list(map(get_event, data.entry[0].get("messaging")))

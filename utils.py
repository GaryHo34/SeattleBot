import requests
from model import Event
from typing import Optional, List


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


def event_parser(event):
    postback = event.get("postback")
    message = event.get("message")
    quick_rp =  message.get('quick_reply') if message else None
    sender_id = event["sender"]["id"]

    return Event(
        type='message' if message else 'postback' if postback else '',
        sender=sender_id,
        text=message.get('text') if message else '',
        quick_reply= quick_rp.get('payload') if quick_rp else '',
        payload=postback.get('payload') if postback else '',
    )

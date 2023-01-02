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
    """
    It makes a GET request to the specified URL,
    and returns the response as a JSON object

    Args:
      url (str): The URL to send the request to.
      headers (Optional[dict]): This is a dictionary of headers that you want to
    send with the request.
      params (Optional[dict]): A dictionary should be encoded into the URL.
      timeout (Optional[int]): The amount of time (in seconds) to wait for the
    server to send data before giving up, as a float, or a (connect timeout, read
    timeout) tuple.

    Returns:
      A dictionary of the response from the API.
    """
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
    """
    It takes a URL, a dictionary of data, a dictionary of headers, and a dictionary
    of parameters, and returns the JSON response from the POST request

    Args:
      url (str): The URL to which the request is to be sent.
      data (dict): The data to be sent in the request body.
      headers (Optional[dict]): A dictionary of HTTP headers to send.
      params (Optional[dict]): A dictionary that should be encoded into the URL.

    Returns:
      A dictionary of the response.
    """
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
    """
    It takes the request body, hashes it with the app secret, and compares it to the
    signature sent in the header. If they match, the request is valid. If they
    don't, the request is invalid

    Args:
      request (Request): Request - The request object.
      X_Hub_Signature_256 (str): str = Header()

    Returns:
      A response object with the content "Invalid request signature." and a status
    code of 401.
    """
    data = await request.body()
    expectedHash = hmac.new(META_APP_SECRET.encode(),
                            data, "sha256").hexdigest()
    if expectedHash != X_Hub_Signature_256[7:]:
        return Response(content="Invalid request signature.", status_code=401)


def get_event(event):
    """
    It takes a Facebook event and returns a Event object

    Args:
      event: The event object that was sent to the webhook.

    Returns:
      A dictionary with the following keys:
        type: 'message' if message else 'postback' if postback else '',
        sender: sender_id,
        text: message.get('text') if message else '',
        quick_reply: quick_rp.get('payload') if quick_rp else '',
        payload: postback
    """
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
    """
    It takes a webhook request data object, checks if the data is valid. If it is,
    then returns a list of events. Else, it returns an empty list.

    Args:
      data (WebhookRequestData): WebhookRequestData

    Returns:
      A list of events
    """
    if data.object != "page" or not data.entry:
        return []

    if not data.entry[0].get("messaging"):
        return []

    return list(map(get_event, data.entry[0].get("messaging")))

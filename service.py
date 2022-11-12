import requests
from typing import Optional

# Wrap requests service for better error handling

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
        return response
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
    headers: Optional[dict] = None,
    params: Optional[dict] = None
):
    try:
        response = requests.post(url=url,
                                 headers=headers,
                                 params=params,
                                 json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    return None

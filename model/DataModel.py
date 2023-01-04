"""This module stores models related to customized data types
"""
from pydantic import BaseModel
from typing import Optional, List


class WebhookRequestData(BaseModel):
    """Stores list of entries received from webhook.

    Args:
        object (str): type of webhook received, valid one should be "page".
        entry (List): list of contents received.

    Attributes:
        object (str): type of webhook received, valid one should be "page".
        entry (List): list of contents received.
    """
    object: str = ""
    entry: List = []


class UserInfo(BaseModel):
    """Stores user's information

    Args:
        recipient_id (str): user's id passed in.
        message_text (:obj: `str`, optional): text sent by user.
        message_type (:obj: `str`, optional): message type used.

    Attributes:
        recipient_id (str): user's id passed in.
        message_text (:obj: `str`): text sent by user.
        message_type (:obj: `str`): message type used.
    """
    recipient_id: str
    message_text: Optional[str] = "None"
    message_type: Optional[str] = "RESPONSE"


class BusinessModel(BaseModel):
    """Stores basic information for each business

    Args:
        name (str): business name.
        address (str): business address.
        rating (str): average rating for the business .
        rating_count (int): number of ratings.

    Attributes:
        name (str): business name.
        address (str): business address.
        rating (str): average rating for the business .
        rating_count (int): number of ratings.
    """
    name: str
    address: str
    rating: str
    rating_count: int

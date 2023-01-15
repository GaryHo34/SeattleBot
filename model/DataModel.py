"""This module stores models related to customized data types
"""
from pydantic import BaseModel
from typing import List


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

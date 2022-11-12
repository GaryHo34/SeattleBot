from pydantic import BaseModel
import typing
from typing import List, Optional


class TextMessage(BaseModel):
    text: str


class WeburlButton(BaseModel):
    type: str = "web_url"
    title: str
    url: str


class PostbackButton(BaseModel):
    type: str = "postback"
    title: str
    payload: str

# Only support quickreply  text + button


class QuickReply(BaseModel):
    content_type: str = "text"
    title: str
    payload: str = ""
    image_url: Optional[str]


class QuickReplyMessage(BaseModel):
    text: str
    quick_replies: List[QuickReply]

# Todo type definition for GENERIC template message

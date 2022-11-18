from pydantic import BaseModel
from typing import List, Optional, Union


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


class PersistentMenu(BaseModel):
    locale: str = "Default"
    composer_input_disable: bool = False
    call_to_actions: List[Union[PostbackButton, WeburlButton]]

from turtle import title
from pydantic import BaseModel
from typing import Optional, List


class RES_TYPE(BaseModel):
    TEXT = "text"
    ATTACHMENT = "attachment"
    QUICK_REPLIES = "quick_replies"
    BUTTONS = "buttons"


class AST_TYPE(BaseModel):
    VIDEO = "video"
    AUDIO = "audio"
    IMAGE = "imgae"
    FILE = "file"


class TEP_TYPE(BaseModel):
    BUTTON = "button"
    GENERIC = "generic"

class BUT_TYPE(BaseModel):
    URL = "web_url"
    POSTBACK = "postback"
    PHONE_NUM = "phone_number"
    ACCOUNT_LINK = "account_link"
    GAME_PLAY = "game_play"


class WebhookRequestData(BaseModel):
    object: str = ""
    entry: List = []


class UserInfo(BaseModel):
    url: str
    page_access_token: str
    recipient_id: str
    message_text: Optional[str] = "None"
    message_type: Optional[str] = "RESPONSE"


RESPONSE_TYPE = RES_TYPE()
ASSET_TYPE = AST_TYPE()
TEMPLATE_TYPE = TEP_TYPE()
BUTTON_TYPE = BUT_TYPE()
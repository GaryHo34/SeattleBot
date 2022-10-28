
from pydantic import BaseModel
from typing import Optional, List


class WebhookRequestData(BaseModel):
    object: str = ""
    entry: List = []


class UserInfo(BaseModel):
    url: str
    page_access_token: str
    recipient_id: str
    message_text: Optional[str] = "None"
    message_type: Optional[str] = "RESPONSE"

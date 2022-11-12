from pydantic import BaseModel
from typing import Optional, List


class WebhookRequestData(BaseModel):
    object: str = ""
    entry: List = []

class UserInfo(BaseModel):
    recipient_id: str
    message_text: Optional[str] = "None"
    message_type: Optional[str] = "RESPONSE"

class BusinessModel(BaseModel):
    name: str
    address: str
    rating: str
    rating_count: int

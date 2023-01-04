from pydantic import BaseModel, constr, conlist, Field
from typing import List, Optional, Union, Literal


class Event(BaseModel):
    type: str
    sender: str
    text: Optional[str]
    quick_reply: Optional[str]
    payload: Optional[str]


class TextMessage(BaseModel):
    text: str


class WeburlButton(BaseModel):
    type: str = "web_url"
    title: constr(max_length=20)
    url: str
    webview_height_ratio: Literal['compact', 'tall', 'full'] = 'full'


class PostbackButton(BaseModel):
    type: str = "postback"
    title: str
    payload: str


class QuickReply(BaseModel):
    content_type: str = "text"
    title: str
    payload: str = ""
    image_url: Optional[str]


class QuickReplyMessage(BaseModel):
    text: str
    quick_replies: List[QuickReply]


class ButtonTemplate(BaseModel):
    template_type: str = "button"
    text: str
    buttons: List[Union[PostbackButton, WeburlButton]]


class DefaultAction(BaseModel):
    type: str = "web_url"
    url: str
    webview_height_ratio: Literal['compact', 'tall', 'full'] = 'full'


class GenericTemplateElement(BaseModel):
    title: str
    subtitle: Optional[str]
    image_url: Optional[str]
    default_action: Optional[DefaultAction]
    buttons: conlist(Union[PostbackButton, WeburlButton], max_items=3)


class GenericTemplate(BaseModel):
    template_type: str = "generic"
    elements: conlist(GenericTemplateElement, max_items=1)


class TemplateMessage(BaseModel):
    type: str = "template"
    payload: Union[ButtonTemplate, GenericTemplate]


class PersistentMenu(BaseModel):
    locale: str = "default"
    composer_input_disabled: bool = False
    call_to_actions: List[Union[PostbackButton, WeburlButton]]

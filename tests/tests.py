import unittest
from model import *


class TestCase(unittest.TestCase):

    # https://developers.facebook.com/docs/messenger-platform/send-messages/buttons
    def test_postback_button(self):
        """
        It tests a postback button.
        """
        expected_button = {
            "type": "postback",
            "title": "<BUTTON_TEXT>",
            "payload": "<STRING_SENT_TO_WEBHOOK>"
        }
        postback_button = PostbackButton(
            title="<BUTTON_TEXT>",
            payload="<STRING_SENT_TO_WEBHOOK>"
        )
        self.assertEqual(expected_button, postback_button.dict())

    def test_weburl_button(self):
        """
        It tests a weburl button.
        """
        expected_button = {
            "type": "web_url",
            "url": "<URL_TO_OPEN_IN_WEBVIEW>",
            "title": "<BUTTON_TEXT>",
            'webview_height_ratio': 'full'
        }
        weburl_button = WeburlButton(
            title="<BUTTON_TEXT>",
            url="<URL_TO_OPEN_IN_WEBVIEW>"
        )
        self.assertEqual(expected_button, weburl_button.dict())

    def test_quickreply(self):
        """
        It tests quick reply.
        """
        expected_reply = {
            "content_type": "text",
            "title": "<TITLE>",
            "payload": "<POSTBACK_PAYLOAD>",
            "image_url": "<URL>"
        }
        quick_reply = QuickReply(
            title="<TITLE>",
            payload="<POSTBACK_PAYLOAD>",
            image_url="<URL>"
        )
        self.assertEqual(expected_reply, quick_reply.dict())

    def test_button_template(self):
        """
        It tests button template.
        """
        expected_template = {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": "What do you want to do next?",
                "buttons": [
                    {
                        "type": "web_url",
                        "url": "https://www.messenger.com",
                        "title": "Visit Messenger",
                        'webview_height_ratio': 'full'
                    }
                ]
            }}
        button_template = TemplateMessage(
            payload=ButtonTemplate(
                text="What do you want to do next?",
                buttons=[WeburlButton(
                    title="Visit Messenger",
                    url="https://www.messenger.com"
                )]
            )
        )
        self.assertEqual(expected_template, button_template.dict())

    def test_generic_template(self):
        """
        It tests generic template.
        """
        expected_template = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Welcome!",
                        "subtitle": "We have the right hat for everyone.",
                        "image_url": "https://petersfancybrownhats.com/company_image.png",
                        "default_action": {
                            "type": "web_url",
                            "url": "https://petersfancybrownhats.com/view?item=103",
                            "webview_height_ratio": "tall",
                        },
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://petersfancybrownhats.com",
                                "title": "View Website",
                                "webview_height_ratio": "full",
                            }, {
                                "type": "postback",
                                "title": "Start Chatting",
                                "payload": "DEVELOPER_DEFINED_PAYLOAD"
                            }
                        ]
                    }
                ]
            }
        }
        generic_template = TemplateMessage(
            payload=GenericTemplate(
                elements=[GenericTemplateElement(
                    title="Welcome!",
                    image_url="https://petersfancybrownhats.com/company_image.png",
                    subtitle="We have the right hat for everyone.",
                    default_action=DefaultAction(
                        url="https://petersfancybrownhats.com/view?item=103",
                        webview_height_ratio="tall",
                    ),
                    buttons=[
                        WeburlButton(
                            title="View Website",
                            url="https://petersfancybrownhats.com",
                        ),
                        PostbackButton(
                            title="Start Chatting",
                            payload="DEVELOPER_DEFINED_PAYLOAD"
                        )
                    ]
                )]
            )
        )
        self.assertEqual(expected_template, generic_template.dict())


if __name__ == '__main__':
    unittest.main()

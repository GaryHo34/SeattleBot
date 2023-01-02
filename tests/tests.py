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
            "title": "<BUTTON_TEXT>"
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


if __name__ == '__main__':
    unittest.main()

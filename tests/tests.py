import unittest
from model import *


class TestCase(unittest.TestCase):

    # https://developers.facebook.com/docs/messenger-platform/send-messages/buttons
    def test_postback_button(self):
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


if __name__ == '__main__':
    unittest.main()

import requests
import logging as logger


class SlackClient:

    @staticmethod
    def slack_post_with_auth(payload=None, auth=None):
        headers = {"Content-Type": "application/json",
                   "authorization": auth}
        url = 'https://slack.com/api/chat.postMessage'

        response = requests.post(url=url, data=payload, headers=headers)
        return response

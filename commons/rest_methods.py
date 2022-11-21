import logging

import requests

from config.get_config import GetConfig


class RestMethods:
    def __init__(self):
        self.config = GetConfig.get_config()

    def post(self, service, url_path, payload=None, headers=None):
        url = self.url(service, url_path)
        logging.info(url)
        response = requests.post(url=url, data=payload, headers=headers)
        return response

    def url(self, service, url_path):
        return f'{self.config[service]}{url_path}'

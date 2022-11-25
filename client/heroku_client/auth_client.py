from client.heroku_client.base_client import BaseClient
import logging

from client.url_path import URL_PATH


class AuthClient(BaseClient):
    def __init__(self):
        super().__init__()

    def auth_get_token(self, payload):
        logging.info('Auth get token api')
        url_path = URL_PATH['auth']
        headers=self.headers.set_json_header()
        response = self.rest_requests.post(self.service, url_path, payload, headers)
        return response.json(), response.status_code,response.text

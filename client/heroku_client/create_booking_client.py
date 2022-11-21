from client.heroku_client.base_client import BaseClient
import logging

from client.url_path import URL_PATH


class CreateBookingClient(BaseClient):
    def __init__(self):
        super().__init__()

    def create_booking(self, payload):
        logging.info('Create booking')
        url_path = URL_PATH['booking']
        self.headers.set_json_header()
        self.headers.add_header_value('Accept','application/json')
        headers =self.headers.get_header()
        logging.info('headers %s',headers)
        response = self.rest_requests.post(self.service, url_path, payload, headers)
        logging.info(response)
        return response.json(), response.status_code,response.text

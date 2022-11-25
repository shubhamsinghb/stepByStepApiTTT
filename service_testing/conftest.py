import json
import logging

import pytest

from client.heroku_client.auth_client import AuthClient
from data_objects.request_entry.auth_entry import AuthRequestEntry
from service_testing.test_data.user_data import USER_DATA


@pytest.fixture
def token_payload():
    def _token_payload(email, password):
        payload = {'username': email,
                   'password': password}
        return payload

    return _token_payload


@pytest.fixture(scope='module')
def get_token():
    payload = AuthRequestEntry(USER_DATA['USER_1']['USERNAME'], USER_DATA['USER_1']['PASSWORD'])
    logging.info("FIXTURE PAYLOAD IS ::: %s" ,payload)
    auth_client = AuthClient()
    response, status_code, text = auth_client.auth_get_token(json.dumps(payload.__dict__))
    return response['token']

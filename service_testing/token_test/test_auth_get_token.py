import json
import logging

from client.heroku_client.auth_client import AuthClient
from data_objects.request_entry.auth_entry import AuthRequestEntry
from service_testing.test_data.user_data import USER_DATA

auth_client = AuthClient()


def test_auth_token():
    payload = {'username': 'admin', 'password': 'password123'}

    response, status_code, text = auth_client.auth_get_token(json.dumps(payload))
    assert status_code == 200
    logging.info("create token response is %s", response)
    assert isinstance(response['token'], str)
    # database asserts


def test_auth_token_with_entry():
    payload = AuthRequestEntry(USER_DATA['USER_1']['USERNAME'], USER_DATA['USER_1']['PASSWORD'])
    response, status_code, text = auth_client.auth_get_token(json.dumps(payload.__dict__))
    assert status_code == 200
    logging.info("create token response is %s", response)
    assert isinstance(response['token'], str)


def test_auth_token_with_fixture(token_payload):
    payload = token_payload(USER_DATA['USER_1']['USERNAME'], USER_DATA['USER_1']['PASSWORD'])

    response, status_code, text = auth_client.auth_get_token(json.dumps(payload))
    assert status_code == 200
    logging.info("create token response is %s", response)
    assert isinstance(response['token'], str)
    # database asserts

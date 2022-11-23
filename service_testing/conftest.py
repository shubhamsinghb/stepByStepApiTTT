import pytest

from client.heroku_client.auth_client import AuthClient


@pytest.fixture
def token_payload():
    def _token_payload(email, password):
        payload = {'username': email,
                   'password': password}
        return payload

    return _token_payload


@pytest.fixture(scope='module')
def get_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    auth_client = AuthClient()
    response, status_code, text = auth_client.auth_get_token(payload)
    return response['token']

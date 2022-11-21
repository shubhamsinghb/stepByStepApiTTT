
import pytest


@pytest.fixture(scope='function')
def login_payload():
    def _login_payload(email, password):
        payload = {'username': email,
                   'password': password}
        return payload

    return _login_payload


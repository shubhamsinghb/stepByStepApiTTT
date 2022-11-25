import json
import logging

import pytest

from client.heroku_client.auth_client import AuthClient

auth_client = AuthClient()


@pytest.mark.parametrize("username , password",
                         [("admin", "password123")])
def test_auth_token_para(username, password):
    payload = {
        "username": username,
        "password": password
    }
    logging.info(json.dumps(payload))

    response, status_code, text = auth_client.auth_get_token(json.dumps(payload))
    assert status_code == 200
    logging.info("create token response is %s", response)
    assert isinstance(response['token'], str)


@pytest.mark.parametrize("username , password, message",
                         [("admin", "password12", "Bad credentials"),
                          ("adin", "password123", "Bad credentials"),
                          ("", "", "Bad credentials"),
                          ])
def test_auth_token_para_negative(username, password, message):
    payload = {
        "username": username,
        "password": password
    }
    logging.info(json.dumps(payload))

    response, status_code, text = auth_client.auth_get_token(json.dumps(payload))
    assert status_code == 200
    logging.info("create token response is %s", response)
    assert response['reason'] == message


@pytest.mark.parametrize("username , password, message",
                         [("admin", "password12", "Bad credentials"),
                          ("adin", "password123", "Bad credentials"),
                          ("", "", "Bad credentials"),
                          ], ids=['worng password', 'wrong user', 'empty password an user'])
def test_auth_token_para_negative_2(username, password, message):
    payload = {
        "username": username,
        "password": password
    }
    logging.info(json.dumps(payload))

    response, status_code, text = auth_client.auth_get_token(json.dumps(payload))
    assert status_code == 200
    logging.info("create token response is %s", response)
    assert response['reason'] == message


@pytest.mark.parametrize("username , password, message",
                         [pytest.param("admin", "password12", "Bad credentials",marks=pytest.mark.wrong_password),
                          pytest.param("adin", "password123", "Bad credentials",marks= pytest.mark.wrong_user),
                          pytest.param("", "", "Bad credentials", marks= pytest.mark.empty_user_password),
                          ], ids=['worng password', 'wrong user', 'empty password an user'])
def test_auth_token_para_negative_3(username, password, message):
    payload = {
        "username": username,
        "password": password
    }
    logging.info(json.dumps(payload))

    response, status_code, text = auth_client.auth_get_token(json.dumps(payload))
    assert status_code == 200
    logging.info("create token response is %s", response)
    assert response['reason'] == message

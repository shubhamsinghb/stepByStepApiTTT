from client.heroku_client.auth_client import AuthClient

auth_client = AuthClient()


def test_auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response, status_code, text = auth_client.auth_get_token(payload)
    print(response)
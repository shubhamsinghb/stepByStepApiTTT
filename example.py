import json
import textwrap

import requests



def print_roundtrip(response, *args, **kwargs):
    format_headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items())
    print(textwrap.dedent('''
        ---------------- request ----------------
        {req.method} {req.url}
        {reqhdrs}

        {req.body}
        ---------------- response ----------------
        {res.status_code} {res.reason} {res.url}
        {reshdrs}

        {res.text}
    ''').format(
        req=response.request,
        res=response,
        reqhdrs=format_headers(response.request.headers),
        reshdrs=format_headers(response.headers),
    ))


def test_if():
    url = "https://restful-booker.herokuapp.com/auth"

    header = {'Content-Type': 'application/json'}

    payload = {
        "username": "admin",
        "password": "password123"
    }
    print(isinstance(header, dict))
    response = requests.post(url, data=json.dumps(payload), headers=header, hooks={'response': print_roundtrip})

    print(response)

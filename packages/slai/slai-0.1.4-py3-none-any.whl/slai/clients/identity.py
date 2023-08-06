import requests

from requests.auth import HTTPBasicAuth
from importlib import import_module

from slai.modules.parameters import from_config

REQUESTS_TIMEOUT = 15


def get_identity_client(*, client_id=None, client_secret=None):
    import_path = from_config(
        "IDENTITY_CLIENT",
        "slai.clients.identity.IdentityClient",
    )
    class_ = import_path.split(".")[-1]
    path = ".".join(import_path.split(".")[:-1])
    return getattr(import_module(path), class_)(
        client_id=client_id, client_secret=client_secret
    )


class IdentityClient:
    BASE_URL = from_config(
        key="BASE_URL",
        default="https://6zacu5yc29.execute-api.us-east-1.amazonaws.com/development",
    )

    def __init__(self, *, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def validate_notebook_auth_token(self, *, token):
        body = {"action": "retrieve", "token": token}

        res = requests.post(
            f"{self.BASE_URL}/app/notebook-auth",
            auth=None,
            headers={},
            json=body,
            timeout=REQUESTS_TIMEOUT,
        )
        res.raise_for_status()
        return res.json()

    def get_user(self):
        body = {"action": "retrieve"}

        res = requests.post(
            f"{self.BASE_URL}/cli/user",
            auth=HTTPBasicAuth(self.client_id, self.client_secret),
            headers={},
            json=body,
            timeout=REQUESTS_TIMEOUT,
        )
        res.raise_for_status()
        return res.json()

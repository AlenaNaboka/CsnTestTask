import requests
from config import register_endpoint


def register_user(user_data):
    return requests.post(register_endpoint, user_data)


def register_successful(user_data):
    response = register_user(user_data)
    assert response.status_code == 200
    return response

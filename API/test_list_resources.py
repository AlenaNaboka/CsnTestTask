import requests
from config import list_resources_endpoint
from testdata import single_resource, list_resource_request_schema
from pytest_schema import schema

'''
The following cases should be validated regarding user login via /login endpoint:
    1. Happy flow: check single resource
    2. Happy flow: check whole structure of the response
    3. Negative flow: invalid username data
'''


def test_single_resources():
    list_resources_response = requests.get(list_resources_endpoint)

    assert list_resources_response.status_code == 200
    assert single_resource in list_resources_response.json()["data"]


def test_list_resource_structure():
    list_resources_response = requests.get(list_resources_endpoint)

    assert schema(list_resource_request_schema) == list_resources_response.json()

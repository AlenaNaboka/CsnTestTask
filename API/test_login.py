import pytest
import requests
from config import login_endpoint
from helper import register_successful
from testdata import user_data, invalid_username_data, invalid_user_pass_data, \
    lack_of_required_field_username, lack_of_required_field_password, not_allowed_user_data

'''
The following cases should be validated regarding user login via /login endpoint:
    1. Happy flow: successful login with valid data
    2. Negative flow: invalid username data
    3. Negative flow: invalid password data
    4. Negative flow: lack of required fields: email
    5. Negative flow: lack of required fields: password
    6. Negative flow: not existed user logins
'''


def test_successful_login():
    register_successful(user_data)

    login_response = requests.post(login_endpoint, user_data)
    assert login_response.status_code == 200
    assert login_response.json()["token"], "(.*)"


@pytest.mark.parametrize("test_input, expected", [(invalid_username_data[0], invalid_username_data[1]["error"]),
                                                  (invalid_user_pass_data[0], invalid_user_pass_data[1]["error"]),
                                                  (lack_of_required_field_username[0],
                                                   lack_of_required_field_username[1]["error"]),
                                                  (lack_of_required_field_password[0],
                                                   lack_of_required_field_password[1]["error"]),
                                                  (not_allowed_user_data[0], not_allowed_user_data[1]["error_login"])])
def test_negative_login(test_input, expected):
    login_response = requests.post(login_endpoint, test_input)

    assert login_response.status_code == 400
    assert login_response.json()["error"] == expected

import re
import pytest
from helper import register_successful, register_user
from testdata import user_data, invalid_username_data, invalid_user_pass_data, \
    lack_of_required_field_username, lack_of_required_field_password, not_allowed_user_data

'''
The following cases should be validated regarding user registration via /register endpoint:
    1. Happy flow: successful registration with valid data
    2. Negative flow: invalid username data
    3. Negative flow: invalid password data
    4. Negative flow: lack of required fields: email
    5. Negative flow: lack of required fields: password
    6. Negative flow: registration for the user is not permitted
'''


def test_successful_registration():
    response = register_successful(user_data)

    assert re.match(".+", response.json()["token"])
    assert re.match("[0-9]+", str(response.json()["id"]))


@pytest.mark.parametrize("test_input, expected", [(invalid_username_data[0], invalid_username_data[1]["error"]),
                                                  (invalid_user_pass_data[0], invalid_user_pass_data[1]["error"]),
                                                  (lack_of_required_field_username[0],
                                                   lack_of_required_field_username[1]["error"]),
                                                  (lack_of_required_field_password[0],
                                                   lack_of_required_field_password[1]["error"]),
                                                  (not_allowed_user_data[0], not_allowed_user_data[1]["error_register"])])
def test_negative_registration(test_input, expected):
    login_response = register_user(test_input)

    assert login_response.status_code == 400
    assert login_response.json()["error"] == expected

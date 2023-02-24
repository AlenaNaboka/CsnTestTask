user_data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

invalid_username_data = [{
    "email": "",
    "password": "pistol"
    },
    {"error": "Missing email or username"}
]

invalid_user_pass_data = [
   {
      "email": "eve.holt@reqres.in",
      "password": ""
   },
   {
      "error": "Missing password"
   }
]

lack_of_required_field_username = [
   {
      "password": "pistol"
   },
   {
      "error": "Missing email or username"
   }
]

lack_of_required_field_password = [
   {
      "email": "eve.holt@reqres.in"
   },
   {
      "error": "Missing password"
   }
]

not_allowed_user_data = [
   {
      "email": "not_allowed_eve.holt@reqres.in",
      "password": "pistol"
   },
   {
      "error_login": "user not found",
      "error_register": "Note: Only defined users succeed registration"
   }
]

single_resource = {
   "id": 1,
   "name": "cerulean",
   "year": 2000,
   "color": "#98B2D1",
   "pantone_value": "15-4020"
}

list_resource_request_schema = {
   "page": int,
   "per_page": int,
   "total": int,
   "total_pages": int,
   "data": list,
   "support": dict
}

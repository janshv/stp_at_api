import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.first_name()
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Update user
update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
patch_data = {
  "email": fake.email(),
  "lastName": fake.last_name(),
  "firstName": fake.first_name(),
  "middleName": fake.first_name()
}
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=update_user_headers, json=patch_data
)
patched_user_response_data = update_user_response.json()
print('Updated user data:', patched_user_response_data)
import httpx

from tools.fakers import get_random_email, get_random_firstname, get_random_lastname

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": get_random_lastname(),
    "firstName": get_random_firstname(),
    "middleName": get_random_firstname()
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())
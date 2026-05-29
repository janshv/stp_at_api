import httpx

from tools.fakers import fake

payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.first_name()
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())
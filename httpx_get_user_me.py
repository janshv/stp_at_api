import httpx

payload = {
    "email": "dmz@mail.org",
    "password": "password"
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)

print("Auth req status code: ", response.status_code)
print("Auth req json: ", response.json())

access_token = response.json()["token"]["accessToken"]

headers = { "Authorization": f"Bearer {access_token}" }

response_at = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print("Me req status code", response_at.status_code)
print("Me req json", response_at.json())
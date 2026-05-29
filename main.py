from httpx import Client, URL, Response, QueryParams

from clients.users.public_users_client import PublicUsersClient
from tools.fakers import fake, get_random_lastname, get_random_firstname

print('Xola!')

usr = {
  "email": fake.email(),
  "password": "12345678",
  "lastName": fake.last_name(),
  "firstName": fake.first_name(),
  "middleName": fake.first_name()
}

puc = PublicUsersClient(Client(base_url="http://localhost:8000"))

dt = puc.create_user_api(request=usr).json()

print(dt)
from httpx import Client, URL, Response, QueryParams

from clients.users.public_users_client import PublicUsersClient
from tools.fakers import get_random_email, get_random_lastname, get_random_firstname

print('Xola!')

usr = {
  "email": get_random_email(),
  "password": "12345678",
  "lastName": get_random_lastname(),
  "firstName": get_random_firstname(),
  "middleName": get_random_firstname()
}

puc = PublicUsersClient(Client(base_url="http://localhost:8000"))

dt = puc.create_user_api(request=usr).json()

print(dt)
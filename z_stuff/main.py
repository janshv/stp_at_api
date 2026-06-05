from httpx import Client, URL, Response, QueryParams, Request
#
# from clients.users.public_users_client import PublicUsersClient
# from tools.fakers import fake
#
# print('Xola!')
#
# usr = {
#   "email": fake.email(),
#   "password": "12345678",
#   "lastName": fake.last_name(),
#   "firstName": fake.first_name(),
#   "middleName": fake.first_name()
# }
#
# puc = PublicUsersClient(Client(base_url="http://localhost:8000"))
#
# dt = puc.create_user_api(request=usr).json()
#
# print(dt)

import requests
import re

Feed_url = "https://outlinekeys.com"
Outline_Feeds = requests.get(Feed_url)
Acc_Key_IDs = re.findall(r'\/key\/(\d+)', Outline_Feeds.text)

for Id in Acc_Key_IDs:
    Acc_Key_url = "https://outlinekeys.com/key/" + Id + "/"
    Acc_key_result = requests.get(Acc_Key_url)
    Acc_Key = re.findall(r'<textarea.*>(.*\/\/.*)<\/textarea>', Acc_key_result.text)
    Acc_Key_Country = re.findall(r'.*#(.*)%.*#', Acc_Key[0])
    print(Acc_Key_Country[0], ":" ,Acc_Key[0])

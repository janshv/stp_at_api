import time
from faker import Faker
from pydantic import EmailStr

fake = Faker()

def get_random_email() -> EmailStr:
    return f"test.{time.time()}@example.com"

def get_random_firstname() -> str:
    return fake.first_name()

def get_random_lastname() -> str:
    return fake.last_name()
import time
from faker import Faker

fake = Faker()

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

def get_random_firstname() -> str:
    return fake.first_name()

def get_random_lastname() -> str:
    return fake.last_name()
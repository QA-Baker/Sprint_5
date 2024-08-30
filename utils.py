import random
import string


def generate_email():
    first_name = ''.join(random.choices(string.ascii_lowercase, k=5))
    last_name = ''.join(random.choices(string.ascii_lowercase, k=7))
    cohort_number = random.randint(100, 999)
    domain = "test.com"
    return f"{first_name}_{last_name}_{cohort_number}@{domain}"


def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password

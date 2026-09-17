import re


def is_valid_email(email):
    pattern = r"^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    pattern = r"^\+?[0-9]{9,15}$"
    return re.match(pattern, phone) is not None

import re

def is_valid_email(email):
    REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    return re.match(REGEX_EMAIL, email)

def is_valid_password(password):
    REGEX_PASSWORD = '^(?=.*[a-zA-Z])(?=.*[!@#$%^~*+=-])(?=.*[0-9]).{8,}$'

    return re.match(REGEX_PASSWORD, password)

def is_valid_phone_number(phone_number):
    REGEX_PHONE = '^\d{3}-\d{3,4}-\d{4}$'

    return re.match(REGEX_PHONE, phone_number)

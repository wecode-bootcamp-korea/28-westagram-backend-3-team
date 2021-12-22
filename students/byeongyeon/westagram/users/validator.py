import re

def validate_email(email):
    is_email_regex = "^[A-Za-z0-9._+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.]+"
    return re.match(is_email_regex, email)

def validate_password(password):
    is_password_regex = "[A-Za-z0-9'~!@#$%^&*()-=,.<>/?]{8,}"
    return re.match(is_password_regex, password)

def validate_mobile(mobile):
    is_mobile_regex = "\d{3}[- .]\d{3,4}[- .]\d{4}"
    return re.match(is_mobile_regex, mobile)
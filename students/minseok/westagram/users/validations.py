import re

from django.core.exceptions import ValidationError

def validation_email(email):
    regex_email = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not re.match(regex_email, email):
        raise ValidationError('Invalid email')

def validation_password(password):
    regex_password = "[\w`~!@#$%^&*(),<.>/?]{8,}"
    
    if not re.match(regex_password, password):
        raise ValidationError('Invalid password')

def validation_phone_number(phone_number):
    regex_phone_number = "\d{3}[- .]\d{3,4}[- .]\d{4}"

    if not (re.match(regex_phone_number, phone_number)):
        raise ValidationError('Invalid phone_number')
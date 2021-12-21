import re

from django.core.exceptions import ValidationError

def validation_email(email):
    REGEX_EMAIL = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not re.match(REGEX_EMAIL, email):
        raise ValidationError('Invalid email')

def validation_password(password):
    REGEX_PASSWORD = "[\w`~!@#$%^&*(),<.>/?]{8,}"
    
    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError('Invalid password')
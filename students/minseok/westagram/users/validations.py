import re

from django.core.exceptions import ValidationError

def validation_email(value):
    regex_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]\b"

    if re.match(regex_email, value):
        return value

    if not (re.match(regex_email, value)):
        raise ValidationError(
            ('%(value)s is invalid email'),
            params={'value': value}
        )
def validation_password(value):
    regex_password = r"[\w`~!@#$%^&*(),<.>/?]{8,}"
    
    if re.match(regex_password, value):
        return value

    if not re.match(regex_password, value):
        raise ValidationError(
            ('%(value)s is invalid password'),
            params={'value': value}
        )

def validation_phone_number(value):
    regex_phone_number = r"\d{3}[- .]\d{3,4}[- .]\d{4}"

    if re.match(regex_phone_number, value):
        return value

    if not (re.match(regex_phone_number, value)):
        raise ValidationError(
            ('%(value)s is invalid phone_number'),
            params={'value': value}
        )
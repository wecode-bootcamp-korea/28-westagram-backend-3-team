import re

from django.core.exceptions import ValidationError

def validate_email(email):
    REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if not re.match(REGEX_EMAIL, email):
        raise ValidationError('EMAIL_INVALIDATION')

def validate_password(password):
    REGEX_PASSWORD = '^(?=.*[a-zA-Z])(?=.*[!@#$%^~*+=-])(?=.*[0-9]).{8,}$'

    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError('PASSWORD_INVALIDATION')

def validate_phone(phone_number):
    REGEX_PHONE = '^\d{3}-\d{3,4}-\d{4}$'

    if not re.match(REGEX_PHONE, phone_number):
        raise ValidationError('PHONE_NUMBER_INVALIDATION')

import re

def is_valid_email(email):
    REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # 일치한 부분을 리턴한다, 일치 하지 않으면 nan을 리턴한다...!
    return bool(re.match(REGEX_EMAIL, email)) # bool 함수의 동작은 python의 특징이다

def is_valid_password(password):
    REGEX_PASSWORD = '^(?=.*[a-zA-Z])(?=.*[!@#$%^~*+=-])(?=.*[0-9]).{8,}$'

    return bool(re.match(REGEX_PASSWORD, password))

def is_valid_phone_number(phone_number):
    REGEX_PHONE = '^\d{3}-\d{3,4}-\d{4}$'

    return bool(re.match(REGEX_PHONE, phone_number))

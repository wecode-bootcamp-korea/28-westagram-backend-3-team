import json
from json.decoder import JSONDecodeError

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import BadRequest

from users.models      import User
from users.validations import is_valid_password, is_valid_email, is_valid_phone_number


# Error codes
#: 중복된 이메일
DUPLICATED_EMAIL        = 'DUPLICATED_EMAIL'
#: 중복된 전화번호
DUPLICATED_PHONE_NUMBER = 'DUPLICATED_PHONE_NUMBER'
#: 중복된 유저아이디
DUPLICATED_USERNAME     = 'DUPLICATED_USERNAME'
#: 잘못된 이메일
INVALID_EMAIL           = 'INVALID_EMAIL'
#: 잘못된 JSON 요청
INVALID_JSON            = 'INVALID_JSON'
#: 잘못된 패스워드
INVALID_PASSWORD        = 'INVALID_PASSWORD'
#: 잘못된 전화번호
INVALID_PHONE_NUMBER    = 'INVALID_PHONE_NUMBER'
#: 인가되지 않은 사용자
INVALID_USER            = 'INVALID_USER'
#: 필수 필드가 입력되지 않음
MISSING_REQUIRED        = 'MISSING_REQUIRED'
#: 이메일 또는 전화번호 중 하나만 입력해야함
TOO_MANY_IDENTIFIERS    = 'TOO_MANY_IDENTIFIERS'


class SignUpView(View):
    def post(self, request):
        try:
            user_info = json.loads(request.body)
        except JSONDecodeError:
            raise BadRequest(INVALID_JSON)

        try:
            email        = user_info.get('email')
            phone_number = user_info.get('phone_number')
            name         = user_info['name']
            username     = user_info['username']
            password     = user_info['password']
        except KeyError:
            raise BadRequest(MISSING_REQUIRED)

        if not email and not phone_number:
            raise BadRequest(MISSING_REQUIRED)
        elif email and phone_number:
            raise BadRequest(TOO_MANY_IDENTIFIERS)
        elif email:
            if not is_valid_email(email):
                raise BadRequest(INVALID_EMAIL)
            if User.objects.filter(email=email).exists():
                raise BadRequest(DUPLICATED_EMAIL)
        else:
            if not is_valid_phone_number(phone_number):
                raise BadRequest(INVALID_PHONE_NUMBER)
            if User.objects.filter(phone_number=phone_number).exists():
                raise BadRequest(DUPLICATED_PHONE_NUMBER)

        if not is_valid_password(password):
            raise BadRequest(INVALID_PASSWORD)

        if User.objects.filter(username=username).exists():
            raise BadRequest(DUPLICATED_USERNAME)

        User.objects.create(
            phone_number = phone_number,
            email        = email,
            name         = name,
            username     = username,
            password     = password
        )

        return JsonResponse({'message':'CREATED'}, status=201)

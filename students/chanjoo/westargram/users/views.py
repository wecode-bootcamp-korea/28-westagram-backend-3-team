import json
from json.decoder import JSONDecodeError

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import BadRequest

from users.models      import User
from users.validations import is_valid_password, is_valid_email, is_valid_phone_number


class SignUpView(View):
    def post(self, request):
        try:
            user_info = json.loads(request.body)
        except JSONDecodeError:
            raise BadRequest('INVALID_JSON')

        try:
            email        = user_info.get('email')
            phone_number = user_info.get('phone_number')
            name         = user_info['name']
            username     = user_info['username']
            password     = user_info['password']
        except KeyError:
            raise BadRequest('KEY_ERROR')

        if not email and not phone_number:
            raise BadRequest('NO_IDENTIFIER')
        elif email and phone_number:
            raise BadRequest('TOO_MANY_IDENTIFIERS')
        elif email:
            if not is_valid_email(email):
                raise BadRequest('INVALID_EMAIL')
            if User.objects.filter(email=email).exists():
                raise BadRequest('DUPLICATED_EMAIL')
        else:
            if not is_valid_phone_number(phone_number):
                raise BadRequest('INVALID_PHONE_NUMBER')
            if User.objects.filter(phone_number=phone_number).exists():
                raise BadRequest('DUPLICATED_PHONE_NUMBER')

        if not is_valid_password(password):
            raise BadRequest('INVALID_PASSWORD')

        if User.objects.filter(username=username).exists():
            raise BadRequest('DUPLICATED_USERNAME')

        User.objects.create(
            phone_number = phone_number,
            email        = email,
            name         = name,
            username     = username,
            password     = password
        )

        return JsonResponse({'message':'CREATED'}, status=201)

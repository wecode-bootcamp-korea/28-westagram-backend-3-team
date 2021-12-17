import json
from re import M

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from users.models      import User
from users.validations import validate_password, validate_phone

class SignUpView(View):
    def post(self, request):
        try:
            user_info = json.loads(request.body)

            phone_number = user_info['phone_number']
            name         = user_info['name']
            username     = user_info['username']
            password     = user_info['password']

            validate_phone(phone_number)
            validate_password(password)

            if User.objects.filter(phone_number=phone_number).exists():
                raise ValidationError('이미 가입된 핸드폰 번호입니다.')

            User.objects.create(
                phone_number = phone_number,
                name         = name,
                username     = username,
                password     = password
            )
            return JsonResponse({'message': 'CREATED'}, status = 201)

        except KeyError as e:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

        except ValidationError as e:
            return JsonResponse({'message': e.message}, status = 400)

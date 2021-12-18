import json

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from users.models      import User
from users.validations import validate_email, validate_password, validate_phone

class SignUpView(View):
    def post(self, request):
        try:
            user_info = json.loads(request.body)

            email        = user_info.get('email')
            phone_number = user_info.get('phone_number')
            name         = user_info['name']
            username     = user_info['username']
            password     = user_info['password']

            # email로 가입한 경우
            if email:
                validate_email(email)

                if User.objects.filter(email=email).exists():
                    raise ValidationError('DUPLICATED_EMAIL')

            # phone_number로 가입한 경우
            if phone_number:
                validate_phone(phone_number)

                if User.objects.filter(phone_number=phone_number).exists():
                    raise ValidationError('DUPLICATED_PHONE_NUMBER')

            # 공통 validation
            validate_password(password)

            if User.objects.filter(username=username).exists():
                raise ValidationError('DUPLICATED_USERNAME')

            User.objects.create(
                phone_number = phone_number,
                email        = email,
                name         = name,
                username     = username,
                password     = password
            )
            return JsonResponse({'message': 'CREATED'}, status = 201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

        except ValidationError as e:
            return JsonResponse({'message': e.message}, status = 400)

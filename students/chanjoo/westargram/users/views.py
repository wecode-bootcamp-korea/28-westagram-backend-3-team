import json
import bcrypt
from json.decoder import JSONDecodeError

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from users.models      import User
from users.validations import is_valid_password, is_valid_email


class SignUpView(View):
    def post(self, request):
        try:
            user_info = json.loads(request.body)

            email    = user_info['email']
            name     = user_info['name']
            username = user_info['username']
            password = user_info['password']

            if not is_valid_email(email):
                raise ValidationError('INVALID_EMAIL')

            if not is_valid_password(password):
                raise ValidationError('INVALID_PASSWORD')

            hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

            if User.objects.filter(email=email).exists():
                raise ValidationError('DUPLICATED_EMAIL')

            if User.objects.filter(username=username).exists():
                raise ValidationError('DUPLICATED_USERNAME')

            User.objects.create(
                email    = email,
                name     = name,
                username = username,
                password = hashed_password
            )

            return JsonResponse({'message':'CREATED'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({'message':e.message}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'INVALID_JSON'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            user_info = json.loads(request.body)

            email    = user_info['email']
            password = user_info['password']

            if not User.objects.filter(email=email).exists():
                raise ValidationError('INVALID_EMAIL')

            hashed_password  = User.objects.get(email=email).password.encode('utf-8')

            if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                raise ValidationError('INVALID_PASSWORD')

            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({'message':e.message}, status=401)

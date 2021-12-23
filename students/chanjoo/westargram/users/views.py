import json
from datetime     import datetime, timedelta
from json.decoder import JSONDecodeError

import bcrypt
import jwt
from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from my_settings       import ALGORITHM, SECRET_KEY
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

            hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

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
                raise ValidationError('INVALID_USER')

            user = User.objects.get(email=email)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                raise ValidationError('INVALID_USER')

            data         = {'id': user.id, 'exp':datetime.now() + timedelta(days=1)}
            access_token = jwt.encode(data, SECRET_KEY, ALGORITHM)

            return JsonResponse({'access_token': access_token}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({'message':e.message}, status=401)

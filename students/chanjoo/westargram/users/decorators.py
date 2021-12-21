import json
import datetime

import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError
from django.http import JsonResponse
from django.contrib.auth.models import User

from my_settings import SECRET_KEY, ALGORITHM
from users.models import User

def login_required(func):
    def wrapper(self, request):
        try:
            access_token = request.headers['Authorization']
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)

            if User.objects.filter(id=payload['user_id']).exists() and payload['exp'] < datetime.now():
                return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message':'NO_TOKEN'}, status=400)

        except DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'}, status=400)

        except ExpiredSignatureError:
            return JsonResponse({'message':'EXPIRED_TOKEN'}, status=401)

    return wrapper

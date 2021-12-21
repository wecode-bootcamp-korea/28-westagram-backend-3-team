import json

import re

from django.http  import JsonResponse
from django.views import View

from .models      import User


# [a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+/.[a-zA-Z0-9.]+
# ‘^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$’
email_validator    = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

password_validator = re.compile('^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,}$')

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not email_validator.match(data['email']):
                return JsonResponse({"message" : "INVALID EMAIL"}, status=400)


            #패스워드에 8자리이상, 문자, 숫자, 특수문자의 조합이 아니라면 에러
            if not password_validator.match(data['password']):
                return JsonResponse({"message" : "INVALID PASSWORD"}, status=400)

            
            #이메일 중복체크, 중복시 에러 반환
            if User.object.filter(email=email).exist():
                return JsonResponse({"message" : "EXISTED EMAIL"}, status=400)


            #위 조건이 아닐시 (정상)
            User.objects.create(
                mobile = data['mobile'],
                email = data['email'],
                username = data['username'],
                user_id = data['user_id'],
                password = data['password']
            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message" : "KEY-ERROR"}, status=400)
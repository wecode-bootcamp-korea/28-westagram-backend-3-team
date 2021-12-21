import json

import re

from django.http  import JsonResponse
from django.views import View

from .models      import User

email_validator    = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
password_validator = re.compile('^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,}$')

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email = data['email']
            password = data['password']

            if not email_validator.match(data['email']):
                return JsonResponse({"message" : "INVALID EMAIL"}, status=400)

            if not password_validator.match(data['password']):
                return JsonResponse({"message" : "INVALID PASSWORD"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EXISTED EMAIL"}, status=400)

            User.objects.create(
                email = email,
                password = password,
                mobile = data['mobile'],
                username = data['username'],
            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY-ERROR"}, status=400)
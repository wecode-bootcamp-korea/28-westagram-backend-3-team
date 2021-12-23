import json

import re
import bcrypt

from django.http  import JsonResponse
from django.views import View

from .models      import User


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            email    = data['email']
            password = data['password']

            REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            REGEX_PASSWORD = '^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,}$'
            
            hashed_password = bcypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()). decode('utf-8')

            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({"message" : "INVALID EMAIL"}, status=400)

            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({"message" : "INVALID PASSWORD"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EXISTED EMAIL"}, status=400)

            User.objects.create(
                email    = email,
                password = hashed_password,
                mobile   = data['mobile'],
                username = data['username'],
            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY-ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)

            if not User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "INVALID EMAIL"}, status=401)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message" : "INCORRECT PASSWORD"}, status=401)
            
            return JsonResponse({"message" : "LOGIN SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY-ERROR"}, status=400)
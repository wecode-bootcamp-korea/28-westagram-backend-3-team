from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError

from users.models import User
from users.validations import validation_email, validation_password, validation_phone_number

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not validation_email(User.email):
                return JsonResponse({"message" : ""}, status=400)

            if not validation_password(User.password):
                return JsonResponse({"message" : "KEY_ERROR"}, status=400)

            if User.objects.filter('email').exists():
                return JsonResponse({"message" : "exists email"}, status=400)

            User.objects.create(
                name = data['name'],
                email = data['email'],
                password = data['password'],
                phone_number = data['phone_number'],
                user_name = data['user_name']
            )

        except ValidationError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        else:
            return JsonResponse({"message" : "SUSSESS"}, status=201)
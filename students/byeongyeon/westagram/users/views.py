# Create your views here.
from django.shortcuts       import render
import json

from django.http            import JsonResponse
from django.views           import View

from users.models           import User
from users.validator        import validate_email, validate_password, validate_mobile

class RegisterView(View):      
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "Email is already in use"}, status=400)
            elif not validate_email(data["email"]):
                return JsonResponse({"message": "Email format is invalid"}, status=400)
            elif not validate_password(data["password"]):
                return JsonResponse({"message": "Password format is invalid"}, status=400)
            elif not validate_mobile(data["mobile"]):
                return JsonResponse({"message": "Mobile number format is invalid"}, status=400)
            else:         
                User.objects.create(
                    name     = data['name'],
                    email    = data['email'],
                    password = data['password'],
                    mobile   = data['mobile'],
                    address  = data['address'],
                    age      = data['age']
                )
        except KeyError:
            return JsonResponse({"message": "Please provide valid information. Check your email, password and mobile number"}, status=400)

        return JsonResponse({"message":"SUCCESS"}, status=201)
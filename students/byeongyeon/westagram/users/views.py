# Create your views here.
import json
import bcrypt

from django.http            import JsonResponse
from django.views           import View

from users.models           import User
from users.validator        import validate_email, validate_password, validate_mobile

class RegisterView(View):      
    def post(self, request):
        data     = json.loads(request.body)
        email    = data["email"]
        password = data["password"]
        mobile   = data["mobile"]

        try:
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "Email is already in use"}, status=400)

            if not validate_email(email):
                return JsonResponse({"message": "Email format is invalid"}, status=400)

            if not validate_password(password):
                return JsonResponse({"message": "Password format is invalid"}, status=400)
                
            if not validate_mobile(mobile):
                return JsonResponse({"message": "Mobile number format is invalid"}, status=400)

            encoded_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                email    = email,
                password = encoded_password,
                mobile   = mobile,
                name     = data['name'],
                address  = data['address'],
                age      = data['age']
            )
            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_CRROR"}, status=400)

class SignInView(View):
    def post(self, request):
        data     = json.loads(request.body)
        email    = data["email"]
        password = data["password"]

        try:
            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            return JsonResponse({"message": "SUCCESS"}, status=200)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)



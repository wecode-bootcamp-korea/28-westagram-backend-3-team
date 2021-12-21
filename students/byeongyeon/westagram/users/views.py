# Create your views here.
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
            if not validate_email(data["email"]):
                return JsonResponse({"message": "Email format is invalid"}, status=400)
            if not validate_password(data["password"]):
                return JsonResponse({"message": "Password format is invalid"}, status=400)
            if not validate_mobile(data["mobile"]):
                return JsonResponse({"message": "Mobile number format is invalid"}, status=400)

            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                mobile   = data['mobile'],
                address  = data['address'],
                age      = data['age']
            )
            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_CRROR"}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            registered_user_password = User.objects.filter(email=data['email'])[0].password         # email은 고유값이므로 [0].password로 비밀번호를 가져온다. 비슷하게 get().password 사용할 수도 있다.
            if data["password"] != registered_user_password:
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            else:
                return JsonResponse({"message": "SUCCESS"}, status=200)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=401)

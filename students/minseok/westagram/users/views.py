#전체 모듈
import json
import bcrypt

#외부 모듈
from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

#내부 모듈
from users.models           import User
from users.validations      import validation_email, validation_password

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            user_name    = data['user_name']

            validation_email(email)
            validation_password(password)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "The email already exists"}, status=400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
                user_name    = user_name
            )
            return JsonResponse({"message" : "SUSSESS"}, status=201)

        except ValidationError as e:
            return JsonResponse({"message" : e.message}, status=400)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class LoginView(View):
    def post(self, request):
        users = json.loads(request.body)
        
        try:
            email    = users['email']
            password = users['password']

            user = User.objects.get(email = email)

            if user.password != password:
                raise ValidationError('Invalid Password')

            return JsonResponse({"message" : "SUSSESS"}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({"message" : e.message})

        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=401)
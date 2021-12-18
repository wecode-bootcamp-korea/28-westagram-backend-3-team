# import json

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views import View
# from users.models import User

# # Create your views here.

# class UserView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         User.objects.create(
#             name = data['name'],
#             email = data['email'],
#             password = data['password'],
#             phone_number = data['phone_number'],
#             user_name = data['user_name'],
#             website = data['website'],
#             introduce = data['introduce'],
#             photo_profile = data['photo_profile']
#         )

#         return JsonResponse({'message' : 'SUCCESS'}, status = 201)

#     def get(self, request):
#         users = User.objects.all()
#         results = []

#         for user in users:

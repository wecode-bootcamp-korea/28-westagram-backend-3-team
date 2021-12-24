from django.urls import path
from users.views import RegisterView, SignInView

urlpatterns = [
    path('/register', RegisterView.as_view()),
    path('/signin', SignInView.as_view())
]
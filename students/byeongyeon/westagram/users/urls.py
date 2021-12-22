from django.urls import path
from users.views import RegisterView, LogInView

urlpatterns = [
    path('/register', RegisterView.as_view()),
    path('/signin', LogInView.as_view())
    ]
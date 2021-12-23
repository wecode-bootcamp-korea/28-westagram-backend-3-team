from django.urls import path
<<<<<<< HEAD
from users.views import RegisterView, SignInView

urlpatterns = [
    path('/register', RegisterView.as_view()),
    path('/signin', SignInView.as_view())
]
=======
from users.views import RegisterView, LogInView

urlpatterns = [
    path('/register', RegisterView.as_view()),
    path('/signin', LogInView.as_view())
    ]
>>>>>>> main

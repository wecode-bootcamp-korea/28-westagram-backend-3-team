from django.urls import path
from users.views import RegisterView

urlpatterns = [
    path('/register', RegisterView.as_view()),                          #/users/register로 httpie 명령어 날릴 것
]

# 앱 actors, movies로 나누어서 작성하는 것이 유지보수에 용이
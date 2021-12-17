from django.db import models

# Create your models here.



class User(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    mobile   = models.PositiveIntegerField(max_length=20)
    age      = models.PositiveIntegerField()
    address  = models.CharField(max_length=500)             #질문사항 : 주소 정도의 텍스트 정보는 TextField 사용이 적합한지?

    class Meta:
        db_table = 'users'


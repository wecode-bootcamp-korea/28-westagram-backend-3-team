from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.CharField(max_length=300, unique=True)
    password     = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=30)

    class Meta:
        db_table = 'users'

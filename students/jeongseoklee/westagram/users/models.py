from django.db import models

class User(models.Model):
    mobile    = models.CharField(max_length=30)
    email     = models.CharField(max_length=100, unique=True)
    username  = models.CharField(max_length=40)
    id        = models.CharField(max_length=50, unique=True)
    password  = models.CharField(max_length=256)

    class Meta:
        db_table: 'users'
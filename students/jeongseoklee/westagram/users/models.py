from django.db import models

class User(models.Model):
    mobile     = models.CharField(max_length=30)
    email      = models.CharField(max_length=100, unique=True)
    username   = models.CharField(max_length=40)
    password   = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
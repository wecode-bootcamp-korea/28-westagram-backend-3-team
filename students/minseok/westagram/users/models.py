from django.db import models

# Create your models here.
class User(models.Model):
    name            = models.CharField(max_length=50)
    email           = models.EmailField(max_length=128, null=True)
    password        = models.CharField(max_length=256)
    phone_number    = models.CharField(max_length=100)
    user_name       = models.CharField(max_length=50)
    website         = models.CharField(max_length=1000, null=True)
    introduce       = models.CharField(max_length=100, null=True)
    profile_image   = models.CharField(max_length=1000, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
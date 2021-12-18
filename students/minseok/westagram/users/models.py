from django.db import models

# Create your models here.
class User(models.Model):
    name            = models.CharField(max_length=50)
    email           = models.EmailField(max_length=128)
    password        = models.CharField(max_length=256)
    phone_number    = models.IntegerField()
    user_name       = models.CharField(max_length=50)
    website         = models.CharField(max_length=300)
    introduce       = models.CharField(max_length=100)
    profile_photo   = models.ImageField()
from django.db import models

class User(models.Model):
    name          = models.CharField(max_length=50)
    password      = models.CharField(max_length=1000)
    phone_number  = models.CharField(max_length=30, null=True)
    username      = models.CharField(max_length=100, unique=True)
    email         = models.EmailField(max_length=200, unique=True)
    date_of_birth = models.DateField(null=True)
    profile_photo = models.CharField(max_length=400, null=True)
    website       = models.URLField(null=True)
    introduction  = models.TextField(blank=True)
    gender        = models.CharField(max_length=20, null=True)
    created_at    = models.DateField(auto_now_add=True)
    updated_at    = models.DateField(auto_now=True)

    class Meta:
        db_table = 'users'

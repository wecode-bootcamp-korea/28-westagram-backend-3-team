# Generated by Django 4.0 on 2021-12-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_date_of_birth_user_gender_user_introduction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]

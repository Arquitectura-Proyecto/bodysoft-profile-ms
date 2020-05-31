# User_model.py
from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=60)
    age = models.IntegerField()
    photo = models.CharField(max_length=200)
    telephone = models.CharField(max_length=10)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name

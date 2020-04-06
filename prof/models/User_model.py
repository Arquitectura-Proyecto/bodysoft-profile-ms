# User_model.py
from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30)
    username = models.CharField(max_length=60)
    age = models.IntegerField()
    photo = models.CharField(max_length=30)
    telephone = models.IntegerField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.username

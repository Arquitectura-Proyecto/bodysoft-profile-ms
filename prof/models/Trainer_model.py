# User_model.py
from django.db import models
from .Speciality_model import Speciality


class Trainer(models.Model):
    trainer_id = models.IntegerField(primary_key=True)
    trainer_name = models.CharField(max_length=60)
    age = models.IntegerField()
    photo = models.CharField(max_length=200)
    telephone = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    sum_ratings = models.IntegerField()
    num_ratings = models.IntegerField()
    description = models.TextField()
    work_experience = models.CharField(max_length=60)
    resources = models.TextField()
    specialities = models.ManyToManyField(Speciality, through="Trainer_speciality")

    def __str__(self):
        return self.trainer_name




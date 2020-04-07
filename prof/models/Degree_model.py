# User_model.py
from django.db import models
from .Trainer_model import Trainer


class Degree(models.Model):
    degree_id = models.AutoField(primary_key=True)
    degree_name = models.CharField(max_length=60)
    year = models.IntegerField()
    institution = models.CharField(max_length=60, )
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.degree_name

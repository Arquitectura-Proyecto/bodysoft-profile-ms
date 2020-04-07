# User_model.py
from django.db import models
from .Trainer_model import Trainer


class Degree(models.Model):
    degree_id = models.CharField(primary_key=True, max_length=30)
    degree_name = models.CharField(max_length=60)
    year = models.IntegerField()
    institution = models.CharField(max_length=60)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE, db_column="trainer_id")

    def __str__(self):
        return self.username

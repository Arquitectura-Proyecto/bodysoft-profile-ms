# User_model.py
from django.db import models
from .Trainer_model import Trainer
from .Speciality_model import Speciality


class Trainer_speciality(models.Model):
    class Meta:
        unique_together = (('trainer', 'speciality'),)

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    def __str__(self):
        return self.trainer

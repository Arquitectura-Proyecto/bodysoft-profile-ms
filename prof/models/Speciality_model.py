# User_model.py
from django.db import models


class Speciality(models.Model):
    speciality_id = models.AutoField(primary_key=True)
    speciality_name = models.CharField(max_length=60)

    def __str__(self):
        return self.speciality_name

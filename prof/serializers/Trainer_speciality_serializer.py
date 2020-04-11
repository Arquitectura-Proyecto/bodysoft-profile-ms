# serializers.py
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from ..models.Trainer_speciality_model import Trainer_speciality
from .Degree_serializer import DegreeSerializer


class TrainerSpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer_speciality
        fields = ('trainer', 'speciality', )

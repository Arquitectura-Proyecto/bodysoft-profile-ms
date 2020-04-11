# serializers.py
from rest_framework import serializers
from ..models.Trainer_model import Trainer
from .Speciality_serializer import SpecialitySerializer


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = ('trainer_id', 'trainer_name', 'age', 'photo', 'telephone',
                  'city', 'sum_ratings', 'num_ratings', 'description', 'work_experience', 'resources', 'specialities', )

# serializers.py
from rest_framework import serializers
from ..models.Trainer_model import Trainer
from .Speciality_serializer import SpecialitySerializer
from rest_framework.serializers import HyperlinkedModelSerializer


class TrainerSerializer(HyperlinkedModelSerializer):
    specialities = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='speciality_name'
    )

    class Meta:
        model = Trainer
        fields = ('trainer_id', 'trainer_name', 'age', 'photo', 'telephone',
                  'city', 'sum_ratings', 'num_ratings', 'description', 'work_experience', 'resources', 'specialities', )
        read_only_fields = ['specialities']

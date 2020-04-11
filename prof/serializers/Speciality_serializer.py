# serializers.py
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from ..models.Speciality_model import Speciality


class SpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Speciality
        fields = ('speciality_id', 'speciality_name', )


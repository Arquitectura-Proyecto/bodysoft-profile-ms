# serializers.py
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from ..models.Degree_model import Degree


class DegreeSerializer(serializers.ModelSerializer):
    trainer = serializers.SlugRelatedField(
        read_only=True,
        slug_field='trainer_id'
    )

    class Meta:
        model = Degree
        fields = ('degree_id', 'degree_name', 'year', 'institution', 'trainer',)
    read_only_fields = ('trainer', )

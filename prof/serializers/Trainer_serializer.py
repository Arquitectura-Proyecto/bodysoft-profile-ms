# serializers.py
from rest_framework.serializers import HyperlinkedModelSerializer
from ..models.Trainer_model import Trainer
from ..models.Degree_model import Degree


class TrainerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ('trainer_id', 'trainer_name', 'age', 'photo', 'telephone',
                  'city', 'sum_ratings', 'num_ratings', 'description', 'work_experience', 'resources',)

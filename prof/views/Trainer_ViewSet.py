
from rest_framework import viewsets
from ..models.Trainer_model import Trainer
from ..serializers.Trainer_serializer import TrainerSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all().order_by('trainer_name')
    serializer_class = TrainerSerializer

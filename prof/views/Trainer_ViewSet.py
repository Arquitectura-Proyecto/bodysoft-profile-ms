
from rest_framework import viewsets, generics
from ..models.Trainer_model import Trainer
from ..serializers.Trainer_serializer import TrainerSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all().order_by('trainer_name')
    serializer_class = TrainerSerializer

    def get_queryset(self):
        queryset = self.queryset
        specialities = self.request.query_params.get('specialities', None)
        if specialities is not None:
            queryset = queryset.filter(specialities=specialities)
        return queryset


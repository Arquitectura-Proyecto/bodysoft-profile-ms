from django.db.models import Prefetch
from django.http import HttpResponse
from rest_framework import viewsets, generics, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.Speciality_model import Speciality
from ..models.Trainer_model import Trainer
from ..serializers.Trainer_serializer import TrainerSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all().order_by('trainer_name')
    serializer_class = TrainerSerializer
    lookup_field = 'specialities'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(
            Prefetch('specialities')
        )
        return queryset

    @action(detail=False)
    def trainers_by_speciality(self, request):
        queryset = self.queryset
        specialities = request.query_params.get('specialities', None)
        if specialities is not None:
            queryset = queryset.filter(specialities=specialities)
        serializer = TrainerSerializer(queryset, many=True)
        return Response(serializer.data)



from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.Trainer_speciality_model import Trainer_speciality

from rest_framework import viewsets, generics, filters, status
from ..models.Trainer_speciality_model import Trainer_speciality
from ..serializers.Trainer_speciality_serializer import TrainerSpecialitySerializer


class TrainerSpecialityViewSet(viewsets.ModelViewSet):
    queryset = Trainer_speciality.objects.all()
    serializer_class = TrainerSpecialitySerializer

    @action(detail=False)
    def get_trainerspeciality(self, request):
        queryset = self.queryset
        trainer = request.query_params.get('trainer', None)
        speciality = request.query_params.get('speciality', None)
        if trainer and trainer is not None:
            queryset = queryset.filter(trainer=trainer, speciality=speciality)
        serializer = TrainerSpecialitySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=["delete"], detail=False)
    def delete_trainerspeciality(self, request):
        queryset = self.queryset
        trainer = request.query_params.get('trainer', None)
        speciality = request.query_params.get('speciality', None)
        if trainer and trainer is not None:
            queryset = queryset.filter(trainer=trainer, speciality=speciality)
            queryset.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

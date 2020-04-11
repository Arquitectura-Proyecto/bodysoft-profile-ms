
from rest_framework import viewsets
from ..models.Speciality_model import Speciality
from ..serializers.Speciality_serializer import SpecialitySerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all().order_by('speciality_name')
    serializer_class = SpecialitySerializer


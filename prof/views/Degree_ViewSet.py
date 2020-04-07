
from rest_framework import viewsets
from ..models.Degree_model import Degree
from ..serializers.Degree_serializer import DegreeSerializer


class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all().order_by('degree_name')
    serializer_class = DegreeSerializer

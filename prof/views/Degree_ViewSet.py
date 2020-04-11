
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.Degree_model import Degree
from ..serializers.Degree_serializer import DegreeSerializer


class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all().order_by('degree_name')
    serializer_class = DegreeSerializer


    @action(detail=False)
    def degrees_by_trainer(self, request):
        queryset = self.queryset
        trainer = request.query_params.get('trainer', None)
        if trainer is not None:
            queryset = queryset.filter(trainer=trainer)
        serializer = DegreeSerializer(queryset, many=True)
        return Response(serializer.data)




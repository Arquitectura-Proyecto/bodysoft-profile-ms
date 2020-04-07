# User_ViewSet.py
from rest_framework import viewsets
from ..models.User_model import User
from ..serializers.User_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_name')
    serializer_class = UserSerializer

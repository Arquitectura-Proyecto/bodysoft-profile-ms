# UserViewSet.py
from rest_framework import viewsets, generics
from ..models.User_model import User
from ..serializers.User_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

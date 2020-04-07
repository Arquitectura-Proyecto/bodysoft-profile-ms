# serializers.py
from rest_framework.serializers import HyperlinkedModelSerializer
from ..models.User_model import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'age', 'user_name', 'photo', 'telephone', 'city',)

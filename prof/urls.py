from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from .views import User_ViewSet, Trainer_ViewSet, Degree_ViewSet, Speciality_ViewSet

router = routers.DefaultRouter()
router.register(r'users', User_ViewSet.UserViewSet)
router.register(r'trainers', Trainer_ViewSet.TrainerViewSet)
router.register(r'degrees', Degree_ViewSet.DegreeViewSet)
router.register(r'specialities', Speciality_ViewSet.DegreeViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from .views import User_ViewSet, Trainer_ViewSet, Degree_ViewSet, Speciality_ViewSet, Trainer_speciality_ViewSet

router = routers.DefaultRouter()
router.register(r'bs-profile-ms/users', User_ViewSet.UserViewSet)
router.register(r'bs-profile-ms/trainers', Trainer_ViewSet.TrainerViewSet)
router.register(r'bs-profile-ms/degrees', Degree_ViewSet.DegreeViewSet)
router.register(r'bs-profile-ms/specialities', Speciality_ViewSet.SpecialityViewSet)
router.register(r'bs-profile-ms/trainerSpecialities', Trainer_speciality_ViewSet.TrainerSpecialityViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
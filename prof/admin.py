from django.contrib import admin
from .models.User_model import User
from .models.Trainer_model import Trainer
from .models.Degree_model import Degree
from .models.Speciality_model import Speciality
from .models.Trainer_speciality_model import Trainer_speciality


admin.site.register(User)
admin.site.register(Trainer)
admin.site.register(Degree)
admin.site.register(Speciality)
admin.site.register(Trainer_speciality)


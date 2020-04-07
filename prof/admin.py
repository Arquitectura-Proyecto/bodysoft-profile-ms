from django.contrib import admin
from .models.User_model import User
from .models.Trainer_model import Trainer
from .models.Degree_model import Degree


admin.site.register(User)
admin.site.register(Trainer)
admin.site.register(Degree)


from django.contrib import admin
from .models import User, Specialty, Appointment


admin.site.register(User)
admin.site.register(Specialty)
admin.site.register(Appointment)


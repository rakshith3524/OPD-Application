from django.contrib import admin
from profiles_api      import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.Appointment)


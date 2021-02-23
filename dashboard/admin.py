from django.contrib import admin
from dashboard import models

# Register your models here.
admin.site.register(models.instructor)
admin.site.register(models.instructor_rate)
admin.site.register(models.student)
admin.site.register(models.rating)
admin.site.register(models.subject)
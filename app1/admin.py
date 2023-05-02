from django.contrib import admin
from .models import ModelClass, Employee, GeeksModel

admin.site.register(GeeksModel)
admin.site.register(ModelClass)
admin.site.register(Employee)


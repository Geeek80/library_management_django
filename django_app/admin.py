from django.contrib import admin
from .models import mymodel, student

# Register your models here.
admin.site.register(mymodel)
admin.site.register(student)
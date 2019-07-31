from django.contrib import admin
from .models import *

# Register your models here.
modelList = [Countries, Cities, Areas]
admin.site.register(modelList)

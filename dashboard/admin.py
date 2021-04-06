from django.contrib import admin
from .models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('country', 'population', 'latitude', 'longitude')


admin.site.register(Data, DataAdmin)

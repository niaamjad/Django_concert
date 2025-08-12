from django.contrib import admin
from .models import concertmodel, locationmodel, timemodel, profilemodel

admin.site.register(concertmodel)
admin.site.register(locationmodel)
admin.site.register(timemodel)


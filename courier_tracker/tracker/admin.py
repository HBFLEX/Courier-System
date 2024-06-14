from django.contrib import admin
from .models import Package, Status, TrackingEvent


admin.site.register([Package, Status, TrackingEvent])

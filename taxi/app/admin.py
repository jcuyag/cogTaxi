from django.contrib import admin
from .models import Ride
# Register your models here.

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ("driver",
                    "status",
                    "user_id", 
                    "first_name", 
                    "last_name", 
                    "destination", 
                    "ride_dt", 
                    "remarks",)
from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = "__all__"


class RideDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            "first_name",
            "last_name",
            "user_id",
            "ride_dt",
            "destination",
            "remarks",
            "status",
            "driver"
        ]
        

class DriverUpdateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            "status"
        ]
    
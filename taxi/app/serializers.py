from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = "__all__"
        depth = 2


class RideDetialSerializer(serializers.ModelSerializer):
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
        ]
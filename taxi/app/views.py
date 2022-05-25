from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status

from .models import Ride
from .serializers import RideSerializer, RideDetailSerializer, DriverUpdateSerialzier

# Create your views here.

class NewRideList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        rides = Ride.objects.filter(status="new")
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)
    

class RideDetailList(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, obj_id):
        return get_object_or_404(Ride, id=obj_id) 
    
    
    def get(self, request, pk, format=None):
        ride = self.get_object(pk)
        serializer = RideDetailSerializer(ride)
        return Response(serializer.data)
    
    
    def put(self, request, pk, format=None):
        ride = self.get_object(pk)
        driver = request.user
        serializer = DriverUpdateSerialzier(ride, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['driver'] = driver
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverBookingList(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        driver = request.user
        rides = Ride.objects.filter(driver=driver)
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)

class AdminBookingList(APIView):
    permission_classes = (IsAdminUser,)
    
    def get(self, request, format=None):
        rides = Ride.objects.all()
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


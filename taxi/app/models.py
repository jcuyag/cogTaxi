import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = [
    ("new", "New"),
    ("booked", "Booked"),
    ("done", "Done")
]

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_id =  models.CharField(max_length=255)
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    ride_dt = models.DateTimeField(auto_now_add=True) 
    destination = models.CharField(max_length=255)
    remarks = models.CharField(max_length=1020)
    status = models.CharField(max_length=255, choices=STATUS)
    
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.urls import reverse

from django.db import models

class Ambulance(models.Model):
    ambulance_number = models.CharField(max_length=20, unique=True)
    ambulance_location = models.CharField(max_length=200)
    driver_name = models.CharField(max_length=100, unique=False, null=False, default='Not Provided!')
    telephone_number = models.CharField(max_length=20, default='Not Provided!', null=True)
    availability = models.BooleanField(default=True)
    # Other fields related to the ambulance

    def __str__(self):
        return f"Ambulance {self.ambulance_number}"


class Booking(models.Model):
    patient_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=200)
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    # Add other fields related to the booking

    def __str__(self):
        return f"Booking {self.id} for {self.patient_name}"



    
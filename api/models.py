from django.db import models

# Create your models here.

class Flight(models.Model): 
  name = models.CharField(max_length=256) 
  airborne = models.BooleanField(default=False)

class Passenger(models.Model): 
  name = models.CharField(max_length=256)

class Seat(models.Model): 
  name = models.CharField(max_length=256) 
  flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="flight")
  passenger = models.ForeignKey(Passenger, on_delete=models.SET_DEFAULT, default=None, related_name='passenger')

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

class Cell(models.Model): 
	type_of_cell = models.CharField(max_length=100)
	habitable = models.BooleanField(default=True)

class Player(models.Model): 
	current_cell = models.ForeignKey(Cell, on_delete=models.PROTECT, related_name='location')
	

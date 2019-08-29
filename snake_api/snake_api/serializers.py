from rest_framework import serializers
from . import models 

class SnakeApiSeralizer(serializers.ModelSerializer): 
  class Meta: 
    fields = ('name', 'airborne')
    model = models.Flight

  class Meta: 
    fields = ('name') 
    model = models.Passenger 

  class Meta: 

    fields = ('name', 'flight', 'passenger')
    model = models.Seat
       
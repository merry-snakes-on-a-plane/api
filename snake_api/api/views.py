from django.shortcuts import render
from rest_framework import generics

from .models import Flight, Passenger, Seat
from snake_api.serializers import SnakeApiSeralizer

class FlightList(generics.ListCreateAPIView): 
  queryset = Flight.objects.all() 
  seralizer_class = SnakeApiSeralizer

class FlightDetail(generics.RetrieveUpdateDestroyAPIView): 
  queryset = Flight.objects.all() 
  seralizer_class = SnakeApiSeralizer

class PassengerList(generics.ListCreateAPIView): 
  queryset = Flight.objects.all() 
  seralizer_class = SnakeApiSeralizer

class PassengerDetail(generics.RetrieveUpdateDestroyAPIView): 
  queryset = Flight.objects.all()
  seralizer_class = SnakeApiSeralizer

class SeatList(generics.ListCreateAPIView): 
  queryset = Seat.objects.all()
  seralizer_class = SnakeApiSeralizer

class SeatDetail(generics.RetrieveUpdateDestroyAPIView): 
  queryset = Flight.objects.all() 
  seralizer_class = SnakeApiSeralizer
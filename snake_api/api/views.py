from django.shortcuts import render
from rest_framework import generics

from .models import Flight, Passenger, Seat
from snake_api.serializers import SnakeApiSeralizer

class FlightList(generics.ListAPIView): 
  queryset = Flight.objects.all() 
  seralizer_class = SnakeApiSeralizer

class FlightDetail(generics.RetrieveAPIView): 
  queryset = Flight.objects.all() 
  seralizer_class = SnakeApiSeralizer

class PassengerList(generics.ListAPIView): 
  queryset = Flight.objects.all() 
  seralizer_class = SnakeApiSeralizer

class PassengerDetail(generics.RetrieveAPIView): 
  queryset = Flight.objects.all()
  seralizer_class = SnakeApiSeralizer

class SeatList(generics.ListAPIView): 
  queryset = Seat.objects.all()
  seralizer_class = SnakeApiSeralizer

class SeatDetail(generics.RetrieveAPIView): 
  queryset = Flight.objects.all() 
  seralizer_class = SnakeApiSeralizer
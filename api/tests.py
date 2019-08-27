from django.test import TestCase
from .models import Flight, Passenger, Seat


# Create your tests here.

class TestCases(TestCase): 
  def setUp(self): 
    flight = Flight.objects.create(name="SureShot")

    passenger = Passenger.objects.create(name="Expendable") 

    seat = Seat.objects.create(name="A1", flight="flight", passenger="passenger")

  def test_flight(self): 
    flight = Flight.objects.get(name="SureShot")

    self.assertEqual(flight.name, "SureShot")

  def test_passenger(self): 
    passenger = Passenger.objects.get(name="Expendable")

    self.assertEqual(passenger.name, "Expendable")

  def test_seat(self): 
    seat = Seat.objects.get(name="A1")

    self.assertEqual(seat.name, "A1")
    self.assertEqual(seat.flight, "flight")
    self.assertEqual(seat.passenger, "passenger")      

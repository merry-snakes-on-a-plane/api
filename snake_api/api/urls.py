from django.urls import path

from . import views

urlpatterns = [
  path('', views.FlightList.as_view()), 
  path('<char:name>/', views.FlightDetail.as_view()), 
  path('passenger/', views.PassengerList.as_view()), 
  path('passenger/<char:name>/', views.PassengerDetail.as_view()),
  path('seat/', views.SeatList.as_view()), 
  path('seat/<char:name>', views.SeatDetail.as_view()),
]
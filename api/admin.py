from django.contrib import admin
from .models import Flight, Passenger, Seat, Cell, Player

# Register your models here.

admin.site.register(Flight)
admin.site.register(Passenger) 
admin.site.register(Seat)
admin.site.register(Cell)
admin.site.register(Player)


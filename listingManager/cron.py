from .models import Reservation

from datetime import datetime

def remove_old_reservations():
    Reservation.objects.filter(ending_date__lte=datetime.now())
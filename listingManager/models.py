from datetime import datetime
import uuid

from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=225)
    rooms = models.ManyToManyField('Room')

class Room(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=225, null=True)

    def reservation(self):
        try:
            reservation =  Reservation.objects.get(room__id=self.id)
        except:
            reservation = Reservation.objects.none()
        return reservation


class Reservation(models.Model):
    tracking_code = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=225)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()
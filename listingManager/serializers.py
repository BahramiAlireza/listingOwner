from rest_framework import serializers

from .models import Room, Reservation


class RoomSerializer(serializers.ModelSerializer):
    is_reserved = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

    def get_is_reserved(self, instance):
        room_reservations = Reservation.objects.filter(room=instance.id, ending_date__gt=self.context['check_datetime'])
        if room_reservations.exists():
            return True
        return False

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        if not data['starting_date'] < data['ending_date']:
            raise serializers.ValidationError({'msg':'The starting date must be before ending date'})
        return data
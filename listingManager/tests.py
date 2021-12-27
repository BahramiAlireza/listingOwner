from datetime import date, datetime, timedelta
from django.test import TestCase, Client
from rest_framework import response

from listingManager.views import ReserveRoom

from .models import Room, Reservation



class CheckApiTestCase(TestCase):

    def setUp(self):
        for i in range(3):
            room = Room.objects.create(number = i, name=f'room{i}')
            if i==1:
                Reservation.objects.create(name="alireza", room=room, starting_date=datetime.now(), ending_date=datetime.now()+timedelta(days=1))
            if i==0:
                Reservation.objects.create(name="alireza2", room=room, starting_date=datetime.now()-timedelta(days=1), ending_date=datetime.now())

    def test_check_api_functionality(self):
        client = Client()
        response = client.get(f'/listing/api/checkrooms/?rooms=1,2,3&datetime={datetime.now().isoformat()}z').json()

        # Expired reservation assertion
        self.assertNotEqual(
            response[0]['is_reserved'], 
            True, 
            "Rooms reservation is expired but is_reserved field shows True"
        )

        # reserved room assertion
        self.assertNotEqual(
            response[1]['is_reserved'], 
            False, 
            'Room is reserved but is_reserved field is False',
        )

        # Not reserved room assertion
        self.assertNotEqual(
            response[2]['is_reserved'], 
            True, 
            'Room has no reservations but is_reserved field is True'
        )

class ReserveApiTestCase(TestCase):
    def setUp(self):
        for i in range(3):
            room = Room.objects.create(number = i, name=f'room{i}')
            self.client = Client()

    def test_reservation_api_functionality(self):
        response = self.client.post('/listing/api/reserve/', {
            'name':'alireza2',
            'room':1,
            'starting_date': f'{datetime.now().isoformat()}Z',
            'ending_date': f'{(datetime.now() + timedelta(days=2)).isoformat()}Z'
        })
        self.assertTrue(Reservation.objects.filter(room=1, ending_date__gt=datetime.now()).exists())

    def test_wrong_date_exception(self):
        response = self.client.post('/listing/api/reserve/', {
            'name':'alireza3',
            'room':1,
            'starting_date': f'{(datetime.now() + timedelta(days=2)).isoformat()}Z',
            'ending_date': f'{datetime.now().isoformat()}Z'
        })
        self.assertEqual(response.status_code, 400)

    def test_reserved_room(self):
        response = self.client.post('/listing/api/reserve/', {
            'name':'alireza2',
            'room':1,
            'starting_date': f'{datetime.now().isoformat()}Z',
            'ending_date': f'{(datetime.now() + timedelta(days=2)).isoformat()}Z'
        })
        response2 = self.client.post('/listing/api/reserve/', {
            'name':'alireza2',
            'room':1,
            'starting_date': f'{datetime.now().isoformat()}Z',
            'ending_date': f'{(datetime.now() + timedelta(days=2)).isoformat()}Z'
        })
        self.assertEqual(response2.status_code, 403)
from datetime import date, datetime
import io as StringIO
from xhtml2pdf import pisa

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from rest_framework import serializers, viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Owner, Reservation, Room
from .serializers import ReservationSerializer, RoomSerializer





class CheckRoom(APIView):
    def get(self, request):
        rooms_id = request.GET.get('rooms').split(',')
        check_datetime = request.GET.get('datetime')
        check_datetime = datetime.fromisoformat(check_datetime[:-1])

        if rooms_id:
            rooms = Room.objects.filter(id__in=rooms_id)
            if rooms.exists():
                return Response(RoomSerializer(rooms, many=True, context={'check_datetime':check_datetime}).data, status=200)
            return Response({'msg': 'No rooms found'}, status=404)

        return Response({'msg':'List of room(s) not provided'}, status=400)


class ReserveRoom(APIView):
    def post(self, request):
        room_reservations = Reservation.objects.filter(room=request.data.get('room'), ending_date__gt=datetime.now())
        if not room_reservations.exists():
            serializer = ReservationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
            return Response({'tracking_code': instance.tracking_code}, status=201)

        return Response({'msg': 'Room is reserved'}, status=403)


def get_report(request, id):
    rooms = Owner.objects.get(id=id).rooms.values_list('id', flat=True)
    room_reservations = Reservation.objects.filter(room__id__in=rooms, ending_date__gt=datetime.now())

    context = {
        'reserves': room_reservations
    }

    template = get_template('report.html')
    html  = template.render(context)
    result = StringIO.BytesIO()

    pdf = pisa.pisaDocument(html, result, encoding="ISO-8859-1")
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % (html))

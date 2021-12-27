from django.urls import path

from .views import CheckRoom, ReserveRoom, get_report
urlpatterns = [
    path('api/checkrooms/', CheckRoom.as_view()),
    path('api/reserve/', ReserveRoom.as_view()),
    path('report/<int:id>/', get_report)
]

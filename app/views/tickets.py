from rest_framework import generics
from app.models import Ticket
from app.serializers.ticket import TicketSerializer


class TicketLC(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

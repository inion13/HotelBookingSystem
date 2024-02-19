from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Hotel, Room, Reservation
from .serializers import HotelSerializer, RoomSerializer, ReservationSerializer, UserSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            return Response({"error": "Только суперпользователь может создавать отели."},
                            status=status.HTTP_403_FORBIDDEN)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def room_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            return Response({"error": "Только суперпользователь может создавать комнаты."},
                            status=status.HTTP_403_FORBIDDEN)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

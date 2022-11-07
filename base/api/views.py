from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import *
from .serializers import * 

@api_view(['GET'])
def getRoutes(request):
    routers = [
        'GET /api'
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routers)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
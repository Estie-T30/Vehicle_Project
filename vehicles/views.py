from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class VehicleListView(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['make', 'model', 'vehicle_type']
    ordering_fields = ['created_at', 'year', 'price']
    ordering = ['-created_at']

# @api_view(['GET'])
# def vehicle_list(request):
#     vehicles = Vehicle.objects.all()
#     serializer = VehicleSerializer(vehicles, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_vehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def retrieve_vehicle(request, id):
    vehicles = get_object_or_404(Vehicle, id=id)
    serializer = VehicleSerializer(vehicles)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_vehicle(request, id):
    vehicles = get_object_or_404(Vehicle, id=id)
    serializer = VehicleSerializer(vehicles, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_vehicle(request, id):
    vehicles = get_object_or_404(Vehicle, id=id)
    vehicles.delete()
    return Response('Vehicle deleted successfully!', status=status.HTTP_204_NO_CONTENT)
    

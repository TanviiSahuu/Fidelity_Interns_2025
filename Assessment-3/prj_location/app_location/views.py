from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from .models import Location
from rest_framework.response import Response
from app_location.serializer import LocationSerializer

class LocationViewSet(viewsets.ViewSet):

    def list(self, request):
        """Retrieve all locations"""
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a single location by pincode"""
        location = get_object_or_404(Location, pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def create(self, request):
        """Create a new location"""
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update an existing location"""
        location = get_object_or_404(Location, pk=pk)
        serializer = LocationSerializer(location, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a location"""
        location = get_object_or_404(Location, pk=pk)
        location.delete()
        return Response({"message": "Location deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

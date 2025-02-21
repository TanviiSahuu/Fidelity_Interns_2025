import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Price
from app_price.serializer import PriceSerializer

class PriceViewSet(viewsets.ViewSet):

    def list(self, request):
        """Retrieve all items"""
        items = Price.objects.all()
        serializer = PriceSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a single item by ID"""
        item = get_object_or_404(Price, pk=pk)
        serializer = PriceSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """Create a new item"""
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update an existing item"""
        item = get_object_or_404(Price, pk=pk)
        serializer = PriceSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete an item"""
        item = get_object_or_404(Price, pk=pk)
        item.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class PriceLocationCustom(viewsets.ViewSet):
    def get_both(self, requests):
        item = Price.objects.all()
        serial = PriceSerializer(item, many=True)

        location_response = requests.get("http://127.0.0.1:8001/locateapp/locate/")
        location_data = location_response.json()

        response_data = {
            "prices": serial.data,
            "locations": location_data
        }

        return Response(response_data)



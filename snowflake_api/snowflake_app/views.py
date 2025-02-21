from django.shortcuts import render
from rest_framework.response import Response
from .models import Trip
from rest_framework import status
from rest_framework.viewsets import ViewSet
from snowflake_app.serializer import tripSerializer

# Create your views here.
class TripViews(ViewSet):
    def list(self,request):
        trp = Trip.objects.all()
        serial = tripSerializer(trp,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        trp = tripSerializer(data=request.data)
        if(trp.is_valid()):
            trp.save()
            return Response(trp.data,status=status.HTTP_200_OK)
        else:
            return Response(trp.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            trp = Trip.objects.get(trip_id=pk)
            serial = tripSerializer(trp)
            return Response(serial.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,pk=None):
        id=pk
        if id is not None:
            trp = Trip.objects.get(trip_id=pk)
            trp.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,pk=None):
        id=pk
        if id is not None:
            trp = Trip.objects.get(trip_id=pk)
            trp = tripSerializer(trp,data=request.data)
            if(trp.is_valid()):
                trp.save()
                return Response(trp.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get_by_date(self, request, trip_date=None):
        trips = Trip.objects.filter(trip_date=trip_date) 
        if not trips.exists():
            return Response({"error": "No trips found for the given date"}, status=status.HTTP_404_NOT_FOUND)

        serial = tripSerializer(trips, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)
        
class TripLimitedViewSet(ViewSet):
    def list(self, request):
        trp = Trip.objects.all()
        serial = tripSerializer(trp, many=True)
        filtered_data = [
            {
                "trip_id": trip["trip_id"],
                "trip_date": trip["trip_date"],
                "trip_boarding": trip["trip_boarding"],
                "trip_destination": trip["trip_destination"]
            }
            for trip in serial.data
        ]

        return Response(filtered_data, status=status.HTTP_200_OK)
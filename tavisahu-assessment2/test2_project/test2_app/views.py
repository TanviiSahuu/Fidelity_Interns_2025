from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import school
from test2_app.serializer import schoolserializer

class schoolListView(generics.ListAPIView):
    queryset = school.objects.all()
    serializer_class = schoolserializer

class schoolCreateView(generics.CreateAPIView):
    queryset = school.objects.all()
    serializer_class = schoolserializer

class schoolRetrieveView(generics.RetrieveAPIView):
    queryset = school.objects.all()
    serializer_class = schoolserializer
    lookup_field = 'schl_id'

class schoolUpdateView(generics.UpdateAPIView):
    queryset = school.objects.all()
    serializer_class = schoolserializer
    lookup_field = 'schl_id'

class schoolDeleteView(generics.DestroyAPIView):
    queryset = school.objects.all()
    serializer_class = schoolserializer
    lookup_field = 'schl_id'
from django.shortcuts import render
from rest_framework.response import Response
from .models import QuestionPaper
from rest_framework import status
from rest_framework.viewsets import ViewSet
from ques_app.serializer import questionSerializer

# Create your views here.
class QuestionViews(ViewSet):
    def list(self,request):
        ques = QuestionPaper.objects.all()
        serial = questionSerializer(ques, many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        ques1 = questionSerializer(data=request.data)
        if(ques1.is_valid()):
            ques1.save()
            return Response(ques1.data,status=status.HTTP_200_OK)
        else:
            return Response(ques1.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            ques2 = QuestionPaper.objects.get(schl_id=pk)
            serial = questionSerializer(ques2)
            return Response(serial.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,pk=None):
        id=pk
        if id is not None:
            ques3 = QuestionPaper.objects.get(schl_id=pk)
            ques3.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,pk=None):
        id=pk
        if id is not None:
            ques4 = QuestionPaper.objects.get(schl_id=pk)
            serial = questionSerializer(ques4,data=request.data)
            if(serial.is_valid()):
                serial.save()
                return Response(serial.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
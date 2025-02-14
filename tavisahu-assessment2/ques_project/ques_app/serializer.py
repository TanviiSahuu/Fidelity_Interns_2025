from rest_framework import serializers
from ques_app.models import QuestionPaper

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPaper
        fields = '__all__'
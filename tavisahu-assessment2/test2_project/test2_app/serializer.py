from rest_framework import serializers
from test2_app.models import school

class schoolserializer(serializers.ModelSerializer):
    class Meta:
        model = school
        fields = '__all__'
from rest_framework import serializers
from snowflake_app.models import Trip

class tripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
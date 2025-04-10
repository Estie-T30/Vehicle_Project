import datetime
from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d %B %Y %I:%M %p', read_only=True)
    updated_at = serializers.DateTimeField(format='%d %B %Y %I:%M %p', read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'

    def validate_year(self, value):
        current_year = datetime.datetime.now().year
        if value < 1886 or value > current_year + 1:
            raise serializers.ValidationError('Year must be between 1886 and {current_year + 1}.')
        return value

    
   
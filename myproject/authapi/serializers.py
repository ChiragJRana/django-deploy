  
from rest_framework import serializers
from .models import Instruments

class InstrumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruments 
        fields = '__all__'

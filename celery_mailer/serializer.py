from rest_framework import serializers
from .models import StudentDetails

class StundetsSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'
        

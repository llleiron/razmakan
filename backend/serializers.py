from rest_framework import serializers
from backend.models import Andznakazm

class AndznakazmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Andznakazm
        fields = '__all__'

class AndznakazmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Andznakazm
        fields = '__all__'

class AndznakazmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Andznakazm
        fields = '__all__'
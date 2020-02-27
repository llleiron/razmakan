from rest_framework import generics
from backend.models import Andznakazm
from backend.serializers import AndznakazmCreateSerializer, AndznakazmDetailSerializer, AndznakazmListSerializer 
# Create your views here.

class AndznakazmCreateAPIView(generics.CreateAPIView):
    serializer_class = AndznakazmCreateSerializer
    queryset = Andznakazm.objects.all()

class AndznakazmListAPIView(generics.ListAPIView):
    serializer_class = AndznakazmListSerializer
    queryset = Andznakazm.objects.all()

class AndznakazmDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AndznakazmDetailSerializer
    queryset = Andznakazm.objects.all()
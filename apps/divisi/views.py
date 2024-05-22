from rest_framework import generics
from apps.divisi.models import Divisi
from apps.divisi.serializers import DivisiSerializer
from rest_framework.permissions import IsAuthenticated


class DivisiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer
    permission_classes = [IsAuthenticated]

class DivisiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer
    permission_classes = [IsAuthenticated]

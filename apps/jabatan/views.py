from rest_framework import generics
from apps.jabatan.models import Jabatan
from apps.jabatan.serializers import JabatanSerializer
from rest_framework.permissions import IsAuthenticated

class JabatanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer
    permission_classes = [IsAuthenticated]

class JabatanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer
    permission_classes = [IsAuthenticated]

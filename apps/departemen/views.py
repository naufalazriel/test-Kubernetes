from rest_framework import generics
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated



class DepartemenListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DepartemenSerializer

    def get_queryset(self):
        id_divisi = self.request.query_params.get('id_divisi')
        queryset = Departemen.objects.all()
        if id_divisi :
            queryset = queryset.filter(divisi_id = id_divisi)
        if not queryset:
            raise NotFound("No Departments found")
        return queryset

class DepartemenRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartemenSerializer
    queryset = Departemen.objects.all()
    permission_classes = [IsAuthenticated]

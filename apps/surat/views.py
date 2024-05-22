from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Surat, Disposisi
from .serializers import SuratSerializer, DisposisiSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from apps.profile.models import Profile
from apps.profile.serializers.serializers_profile import UserSerializer
from apps.profile.serializers.serializers_profile import ProfileSerializer


class SuratListCreateView(generics.ListCreateAPIView):
    queryset = Surat.objects.all()
    serializer_class = SuratSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Surat.objects.all()
        status = self.request.query_params.get('status', None)
        kategori = self.request.query_params.get('kategori', None)

        if status is not None:
            queryset = queryset.filter(status=status)
        if kategori is not None:
            queryset = queryset.filter(kategori=kategori)
        
        return queryset
    
class SuratRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Surat.objects.all()
    serializer_class = SuratSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        # Get penerima_detail using UserSerializer
        penerima_detail = []
        for user_id in data['penerima']:
            user = Profile.objects.get(id=user_id)
            user_serializer = ProfileSerializer(user)
            penerima_detail.append(user_serializer.data)
        
        # Get penyetuju_detail using UserSerializer
        penyetuju_detail = []
        for user_id in data['penyetuju']:
            user = Profile.objects.get(id=user_id)
            user_serializer = ProfileSerializer(user)
            penyetuju_detail.append(user_serializer.data)
        
        data['penerima'] = penerima_detail
        data['penyetuju'] = penyetuju_detail

        return Response(data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DisposisiListCreateView(generics.ListCreateAPIView):
    queryset = Disposisi.objects.all()
    serializer_class = DisposisiSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        return Response(serializer.data)
    
class DisposisiRetrieve(generics.RetrieveAPIView):
    queryset = Disposisi.objects.all()
    serializer_class = DisposisiSerializer
from rest_framework import generics
from apps.profile.models import *
from apps.profile.serializers.serializers_profile import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated



class ProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id_user = self.request.query_params.get('id_user')
        id_jabatan = self.request.query_params.get('id_jabatan')
        id_departemen = self.request.query_params.get('id_departemen')
        queryset = Profile.objects.all()
        if id_user :
            queryset = queryset.filter(user_id = id_user)
        elif id_departemen :
            queryset = queryset.filter(departemen_id = id_departemen)
        elif id_jabatan :
            queryset = queryset.filter(jabatan_id = id_jabatan)
        

        if not queryset:
            raise NotFound("User not found!")
        return queryset
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfileUpdateRetrieveAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'user_id'
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        id = self.kwargs[self.lookup_field]
        queryset = Profile.objects.filter(user_id = id)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True, context={'request': request}) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
class SekretarisListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SekretarisSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id_user = self.request.query_params.get('id_user')
        try:
            profile = Profile.objects.get(user_id=id_user)
        except Profile.DoesNotExist:
            raise NotFound("User not found!")

        queryset = Sekretaris.objects.all()
        if profile:
            queryset = queryset.filter(atasan_id=profile.id)
        return queryset
    
    def post(self, request):
        serializer = SekretarisSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class SekretarisUpdateRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SekretarisSerializer
    queryset = Sekretaris.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DelegasiListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DelegasiSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id_user = self.request.query_params.get('id_user')

        try:
            profile = Profile.objects.get(user_id=id_user)
        except Profile.DoesNotExist:
            raise NotFound("User not found!")

        queryset = Delegasi.objects.all()
        if profile :
            queryset = queryset.filter(atasan_id = profile.id)
        return queryset
    
    def post(self, request):
        serializer = DelegasiSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DelegasiUpdateRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DelegasiSerializer
    queryset = Delegasi.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
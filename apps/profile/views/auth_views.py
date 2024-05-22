from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from apps.profile.serializers.serializers_auth import *
from apps.profile.serializers.serializers_profile import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from datetime import datetime as dt
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# class IsAuthenticatedAndTokenExists(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # token = request.COOKIES.get('jwt')
#         token = request.session.get('user')['jwt']

#         if not token:
#             return False

#         try:
#             decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             exp_timestamp = decoded_token.get('exp')
#             if exp_timestamp:
#                 exp_datetime = dt.utcfromtimestamp(exp_timestamp).replace(tzinfo=None)
#                 if exp_datetime < dt.utcnow():
#                     # Token sudah kadaluwarsa
#                     return False
#             else:
#                 # Token tidak memiliki waktu kadaluarsa
#                 return False
            # Token valid dan belum kadaluwarsa
        #     return True
        # except jwt.ExpiredSignatureError:
        #     raise AuthenticationFailed('Token expired, please log in again.')
        # except jwt.InvalidTokenError:
        #     raise AuthenticationFailed('Invalid token, please log in again.')

class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        user = User.objects.filter(username=username).first()
        if user :
            raise AuthenticationFailed('User is already!')

        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        token = RefreshToken.for_user(user)
        
        if user and user.check_password(password):
            # Generate JWT token
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
                'iat': datetime.datetime.utcnow()
            }
            # token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            
            # Create a response object
            response = Response({
                'id': user.id,
                'username': username,
                'jwt': str(token.access_token)
            })
            
            return response
        else:
            return Response({'message': 'Invalid credentials'}, status=400)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.delete_cookie('id')
        response.data = {
            'message': 'Logout Success!'
        }
        return response 
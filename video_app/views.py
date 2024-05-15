from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
# videoapp/views.py
 
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
# from .models import Campaign, Recording
# from .models import AutoAttendantEntry
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from .models import CustomUser
from rest_framework import generics
# from .models import BlasterCall
# from .serializers import BlasterCallSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
# from .models import CustomUser, DetailedAICall
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework .views import APIView
import csv
import requests
import pytz
import datetime
from django.utils import timezone
from functools import wraps
import ast
import uuid
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from video_app.models import VideoProject
from .models import VideoProject
from video_app.serializers import VideoProjectSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import VideoProjectSerializer
import jwt
from functools import wraps
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser

def jwt_authentication_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            token = token.split(" ")[1]
            decoded_token = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = decoded_token.get('id')
            user = CustomUser.objects.get(pk=user_id)
            request.user = user
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token!')
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('User not found!')

        return view_func(request, *args, **kwargs)

    return wrapper


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response(serializer.data)
        return Response({
            'message': 'User registered successfully',
            'user': serializer.data
        })
        


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not (email or phone_number):
            raise AuthenticationFailed('Email or phone number is required!')

        if email:
            # If email is provided, search for the user by email
            user = CustomUser.objects.filter(email=email).first()
        else:
            # If email is not provided but phone number is, search for the user by phone number
            user = CustomUser.objects.filter(phone_number=phone_number).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        # Create a JWT token
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        # Return the JWT token in the response
        response_data = {
            'message': 'Login successful',
            'token': token,
            'user_id': user.id
        }
        response = JsonResponse(response_data)

        # Set the JWT token as a cookie
        response.set_cookie(key='jwt', value=token, httponly=True)

        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'logout success'
        }
        return response




from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.response import Response
from .models import VideoProject
from .serializers import VideoProjectSerializer
from .decorators import jwt_authentication_required  # Correct import

# @method_decorator(csrf_exempt, name='dispatch')
# @method_decorator(jwt_authentication_required, name='dispatch')
class VideoProjectListCreate(generics.ListCreateAPIView):
    queryset = VideoProject.objects.all()
    serializer_class = VideoProjectSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        return Response({"message": "Video project created successfully", "data": data}, status=status.HTTP_201_CREATED)

class VideoProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoProject.objects.all()
    serializer_class = VideoProjectSerializer






# crud..api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import VideoProject
from .serializers import VideoProjectSerializer
from rest_framework.response import Response
from rest_framework import status

# @method_decorator(csrf_exempt, name='dispatch')
# @method_decorator(jwt_authentication_required, name='dispatch')
# @api_view(['POST', 'GET'])
# def video_project_list(request):
#     if request.method == 'POST':
#         serializer = VideoProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('Video project created successfully', status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'GET':
#         video_projects = VideoProject.objects.all()
#         serializer = VideoProjectSerializer(video_projects, many=True)
#         return Response(serializer.data)

# @method_decorator(csrf_exempt, name='dispatch')
# @method_decorator(jwt_authentication_required, name='dispatch')
# @api_view(['PUT', 'DELETE'])
# def video_project_detail(request, pk):
#     try:
#         video_project = VideoProject.objects.get(pk=pk)
#     except VideoProject.DoesNotExist:
#         return Response('Video project does not exist', status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = VideoProjectSerializer(video_project, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('Video project updated successfully', status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         video_project.delete()
#         return Response('Video project deleted successfully', status=status.HTTP_204_NO_CONTENT)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import VideoProject
from .serializers import VideoProjectSerializer
from .decorators import jwt_authentication_required  # Import your custom decorator

@api_view(['POST', 'GET'])
@jwt_authentication_required
def video_project_list(request):
    if request.method == 'POST':
        serializer = VideoProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Video project created successfully', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        video_projects = VideoProject.objects.all()
        serializer = VideoProjectSerializer(video_projects, many=True)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@jwt_authentication_required
def video_project_detail(request, pk):
    try:
        video_project = VideoProject.objects.get(pk=pk)
    except VideoProject.DoesNotExist:
        return Response('Video project does not exist', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = VideoProjectSerializer(video_project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Video project updated successfully', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        video_project.delete()
        return Response('Video project deleted successfully', status=status.HTTP_204_NO_CONTENT)

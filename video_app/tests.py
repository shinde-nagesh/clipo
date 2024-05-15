

# Create your tests here.
# Import necessary modules

from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import VideoProject

class CreateVideoProjectTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user and obtain an authentication token
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = self.get_token()

    def get_token(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'}, format='json')
        return response.data['token']

    def test_create_video_project(self):
        data = {
            "title": "Test Video",
            "description": "This is a test video project.",
            "creation_date": "2024-05-15",
            "status": "active"
        }
        # Include token in request headers
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post('/api/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VideoProject.objects.count(), 1)
        
        # Print success message if the request is successful
        if response.status_code == status.HTTP_201_CREATED:
            print("Video project created successfully")

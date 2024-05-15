"""
URL configuration for videoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from video_app import views
from video_app.views import VideoProjectListCreate, VideoProjectDetail,RegisterView,LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', VideoProjectListCreate.as_view(), name='project-list'),
    
    path('projects/<int:pk>/', VideoProjectDetail.as_view(), name='project-detail'),
    
    path('register/', RegisterView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/', views.video_project_list, name='video_project_list'),
    # path('api/video-projects/<int:pk>/', views.video_project_detail, name='video_project_detail'),
    path('api/<int:pk>/', views.video_project_detail, name='video_project_detail')
]



from django.urls import path

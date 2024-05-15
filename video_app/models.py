from django.db import models

# Create your models here.
# video_app/models.py

# from django.db import models

# class VideoProject(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     creation_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='active')

#     def __str__(self):
#         return self.title
from django.db import models

class VideoProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')
    # file = models.FileField(upload_to='videos/')  # Define the file field with upload_to parameter to specify upload directory

    def __str__(self):
        return self.title


from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, Group,Permission
from django.utils.translation import gettext_lazy as _


from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import Permission  # Corrected import
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Add phone_number field
    # party = models.CharField(max_length=100) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Add unique related_name attributes for groups and user_permissions fields for superusers
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_super_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_super_permissions',
        help_text=_('Specific permissions for this superuser.'),
    )

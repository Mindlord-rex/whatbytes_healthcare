from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
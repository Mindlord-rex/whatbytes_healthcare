from django.db import models
from accounts.models import User
# Create your models here.

class Patient(models.Model):
    
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_history = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
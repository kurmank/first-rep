from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    telephone_number = models.CharField(max_length=25, blank=False)

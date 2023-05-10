from django.db import models
from django.contrib.auth.models import AbstractUser
    

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='images')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']
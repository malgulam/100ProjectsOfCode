from django.db import models

# Create your models here.

class User(models.Model):
    username    = models.CharField(max_length=20)
    password    = models.BinaryField(max_length=255)
    date_joined = models.DateTimeField(auto_now=True, blank=True)
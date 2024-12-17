from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=100)

class Deleted(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=100)

    

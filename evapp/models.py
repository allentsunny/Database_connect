from django.db import models
 
class register(models.Model):
    username=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)


# Create your models here.

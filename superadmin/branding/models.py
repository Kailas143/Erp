from django.db import models

# Create your models here.
class Registered_users(models.Model) :
    name =models.CharField(max_length=1024)
    company=models.CharField(max_length=1024) 
    email =models.EmailField(max_length=254,unique=True)
    domain=models.CharField(max_length=1024)
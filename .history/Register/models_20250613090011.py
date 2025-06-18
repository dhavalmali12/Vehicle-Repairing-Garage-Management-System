from django.db import models

# Create your models here.

class Register(models.Model):
    Full_Name=models.CharField(max_length=60)
    Email_ID=models.CharField(max_length=50)
    Password=models.CharField(max_length=60)
    Confirm_Password=models.CharField(max_length=60)    
    
    

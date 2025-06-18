from django.db import models

class Booking_Model(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.IntegerField(max_length=10)
    Email_Id=models.EmailField(max_length=50)
    Car_Model=models.CharField(max_length=5)
    Service = models.CharField(max_length=20, choices=(
        ('Engine Repair', 'Engine Repair'),
        ('Battery Check & Replacement', 'Battery Check & Replacement'),
        ('Completed', 'Completed')
    ))
    date_time=models.DateTimeField(max_length=10)
    Message=models.CharField(max_length=200)
    

# Create your models here.

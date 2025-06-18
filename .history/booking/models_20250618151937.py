from django.db import models

class Booking_Model(models.Model):
    full_Name=models.CharField(max_length=50)
    phone_Number=models.IntegerField()
    email_Id=models.EmailField(max_length=50)
    car_Model=models.CharField(max_length=5)
    service = models.CharField(max_length=100, choices=(
        ('Engine Repair', 'Engine Repair'),
        ('Battery Check & Replacement', 'Battery Check & Replacement'),
        ('brake', 'brake'),
        ('AC & Electrical System Repair','AC & Electrical System Repair')
    ))
    date_time=models.DateTimeField(max_length=10)
    message=models.CharField(max_length=200)
    

# Create your models here.

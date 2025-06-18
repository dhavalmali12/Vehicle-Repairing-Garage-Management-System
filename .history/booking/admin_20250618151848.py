from django.contrib import admin
from booking.models import Booking_Model



class Register_Admin(admin.ModelAdmin):
    list_display=("Full_Name","Phone_Number"," Email_Id"," Car_Model","  Service"," date_time","Message")
    
admin.site.booking(Booking_Model,Register_Admin)    

# Register your models here.

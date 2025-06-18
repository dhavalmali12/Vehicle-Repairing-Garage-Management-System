from django.contrib import admin
from booking.models import Booking_Model



class Register_Admin(admin.ModelAdmin):
    list_display=("full_Name","phone_Number","email_Id","car_Model","service","date_time","message")
    
admin.site.register(Booking_Model,Register_Admin)    


# Register your models here.

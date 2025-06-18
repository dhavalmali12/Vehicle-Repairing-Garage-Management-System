from django.contrib import admin
from Register.models import Register_Model


class Register_Admin(admin.ModelAdmin):
    list_display=("Full_Name","Phone_Number"," Email_Id"," Car_Model","  Service"," date_time","Message")

# Register your models here.

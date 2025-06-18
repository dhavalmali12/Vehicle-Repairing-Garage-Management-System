from django.contrib import admin
from Register.models import Register_Model

class RegisterAdmin(admin.ModelAdmin):
    list_display=(" Full_Name"," Email_ID", "Password","Confirm_Password")

admin.site.register(Service,ServiceAdmin)    

# Register your models here.

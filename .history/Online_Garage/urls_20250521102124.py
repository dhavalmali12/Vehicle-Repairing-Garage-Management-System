"""
URL configuration for Online_Garage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Online_Garage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views. Login),
    path('register/',views.Register),
    path('engine_Service/',views.Engine_Service),
    path('battery_Service/',views.Battery_Service),
    path('brake_Service/',views.Brake_Service),
    path('ac_Service/',views.Ac_Service),
    path('booking/',views.Booking),
    path('offer/',views.Offer),
    path('about/',views.About),
    path('contact/',views.Contact),
    path('header/',views.Header),
    path('footer/',views.Footer),
    path('userform/',views.UserForm,name="userfrom"),
    path('hello/',views.hello,name='hello'),
    path('submitform/',views.Submitform name="submitform")
    
    
]

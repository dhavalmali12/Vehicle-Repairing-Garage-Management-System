from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from.forms import UsersForms

def index (request):
    return render(request,"1_index.html")

def Login (request):
    e=""
    p=""
    try:
        if request.method=="POST":
            e=request.POST.post('email')
            p=request.POST.post('password')
    except:
        pass        
    return render(request,"3_Login.html",{'email':e,"password":p})

def Register (request):
    return render(request,"4_Register.html")


def Engine_Service(request):
    return render(request,"5_EngineService.html")

def Battery_Service (request):
    return render(request,"6_batteryService.html")

def Brake_Service (request):
    return render(request,"7_Brake.html")

def Ac_Service(request):
    return render(request,"8_Ac.html")

def Booking (request):
    return render(request,"9_Booking.html")

def Offer (request):
    return render(request,"10_offer.html")

def About (request):
    return render(request,"11_About.html")

def Contact (request):
    return render(request,"12_Contact.html")

def Header(request):
    return render(request,"13_Header.html")

def Footer(request):
    return render(request,"14_Footer.html")

def hello(request):
    if request.method=="GET":
       output=request.GET.get("output")
    return render(request,"16_hello.html",{"output":output})

def UserForm(request):
    finalans=0
    fn=UsersForms()
    data={'form':fn}
    try:
     if request.method=="POST":
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        finalans=n1+n2
        data={
              'form':fn,
              'output':finalans
          }
        # url="/hello/?output={}".format(finalans)
        # return redirect(url)

    except:
        pass
    return render(request,"15_UserForm.html",data)    


def Submitform(request):
   
    try:
        if request.method=="POST":
          n1=int(request.POST.get("num1"))
          n2=int(request.POST.get("num2"))
          finalans=n1+n2
          data={
              'n1':n1,
              'n2':n2,
              'output':finalans
          }
        return HttpResponse(f"Result:{finalans}")
    except Exception as e:
        return HttpResponse(f"Error:{str(e)}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # finalans=0
    # data={}
    # try:
    #     if request.method=="POST":
    #      n1=int(request.POST['value1'])
    #      n2=int(request.POST['value2'])
    #      finalans=n1+n2
    #      data={
    #          'n1':n1,
    #          'n2':n2,
    #          'output':finalans
    #      }
    #      url='/hello/?output={}'.format(finalans)
         
    #      return HttpResponseRedirect(url)
    # except:
    #     pass    
    
    # return render(request,"15_UserForm.html",data)
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from.forms import UsersForms

def index (request):
    return render(request,"1_index.html")

def About (request):
 return render(request,"11_About.html")

def Login (request):
    email=""
    password=""
    data={}
    try:
       
        email=request.POST.get('value1')
        password=request.POST.get('value2')
        data={
            'email':email,
            'password':password,
          
        }
        url="/hello/?output={}".format(data)
        return HttpResponseRedirect(url)
    except:
        pass   
    return render(request,"3_Login.html")

def hello(request):
    email=request.GET.get('email')
    password=request.GET.get('password')
    
    context={
        'email':email,
        'password':password
    }
    return render (request,"16_hello.html",context)
    
    

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


def Contact (request):
    return render(request,"12_Contact.html")

def Header(request):
    return render(request,"13_Header.html")

def Footer(request):
    return render(request,"14_Footer.html")

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
        url="/hello/?output={}".format(finalans)
        return redirect(url)

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
    
    
def calculator(request):
    c=''
    
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr == "+":
                c=n1+n2
            elif opr == "-":
                c=n1-n2    
            elif opr == "*":
                c=n1*n2    
            elif opr == "/":
                c=n1/n2    
            
    except:
        d="invalid opr..."
    print(c)   
    return render(request,"17_calculator.html",{"c":c})
    
    
def evenodd(request):
    a=''
    if request.method=="POST":
     n1=int(request.POST.get('num1'))
     if n1%2==0:
      a="Even"
     else:
      a="Odd"
                
    return render(request,"18_EvenAndOdd.html",{"a":a})
 
 
def marksheet(request):
    percentage=""
    final=""
    total=""
    if request.method=="POST":
        n1=int(request.POST.get('sub1'))
        n2=int(request.POST.get('sub2'))
        n3=int(request.POST.get('sub3'))
        n4=int(request.POST.get('sub4'))
        n5=int(request.POST.get('sub5'))
        total=n1+n2+n3+n4+n5
        percentage=(total/500)*100
        
        if(percentage>90 and percentage<=100):
            final="A"
        elif(percentage>80 and percentage<=90):
            final="B"
        elif(percentage>70 and percentage<=80):
            final="C"
        elif(percentage>60 and percentage<=70):
            final="D"
        elif(percentage>50 and percentage<=60):
            final="E"
        elif(percentage>40 and percentage<=50):
            final="F"
        elif(percentage>=33 and percentage<=40):
            final="G"
        else:
            print("FAIL TRY NEXT YEAR:")
        
    
    return render(request,"19_Marksheet.html",{'final':final,'percentage':percentage}) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
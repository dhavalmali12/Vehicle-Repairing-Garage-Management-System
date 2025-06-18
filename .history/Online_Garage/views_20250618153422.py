from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from.forms import UsersForms
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from Register.models import Register_Model
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from booking.models import Booking_Model

def newsDetails(request,slug):
    newsDetails=News.objects.get(news_slug=slug)
    
    data={
        'newsDetails':newsDetails
    }
    return render(request,"20_newsDetails.html",data)

def index (request):
    
   
    NewsData=News.objects.all().order_by('News_title')[:2]
    serviceData=Service.objects.all()
    paginator=Paginator(serviceData,2)
    page_number=request.GET.get('page')
    serviceDataFinal=paginator.get_page(page_number)
    totalpage=serviceDataFinal.paginator.num_pages #3
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            serviceData=Service.objects.filter(service_title__icontains=st)
    
    data={
        'serviceData':serviceDataFinal,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)],
        "newsData":NewsData
    }
    return render(request,"1_index.html",data)

def About (request):
    
    subject="Testing Mail"
    form='malidhavalk113@gmail.com'
    msg='<h1>Hello Guys<h1><b>Kaise Hai Aaplog</b>'
    to='dkgelot13@gmail.com'         
    ms=EmailMultiAlternatives(subject,msg,form,[to])
    ms.content_subtype='html'
    ms.send()

    
    #  send_mail(
    #     'Testing Mail',
    #     'Here is the message',
    #     'malidhavalk113@gmail.com',
    #     ['dkgelot13@gmail.com'],
    #     fail_silently=True
    # )
    return render(request,"11_About.html")

def Login (request):
    # email=""
    # password=""
    # data={}
    # try:
       
    #     email=request.POST.get('value1')
    #     password=request.POST.get('value2')
    #     data={
    #         'email':email,
    #         'password':password,
          
    #     }
    #     # url="/hello/?output={}".format(data)
    #     # return HttpResponseRedirect(url)
    # except:
    #     pass   
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
    
    message=''
    if request.method=="POST":
        name=request.POST.get('Full-name')
        Email=request.POST.get('Email-Id')
        Password=request.POST.get('Password')
        Confirm_password=request.POST.get('Confirm_password')
        data=Register_Model(Full_Name=name, Email_ID=Email, Password=Password,Confirm_Password=Confirm_password)
        data.save()
        message="YOUR DATA IS SUCCESSUFULLY INSERTED"
        return HttpResponseRedirect("/login")  

    
    return render(request,"4_Register.html",{"message":message})



def Engine_Service(request):
    return render(request,"5_EngineService.html")


def Battery_Service (request):
    return render(request,"6_batteryService.html")

def Brake_Service (request):
    return render(request,"7_Brake.html")

def Ac_Service(request):
    return render(request,"8_Ac.html")

def Booking (request):
    if request.method=="POST":
        name=request.post.get("name")
        phone=request.post.get("phone")
        email=request.post.get("email")
        car_model=request.post.get("car-model")
        service=request.post.get("service")
        date=request.post.get("date")
        message=request.post.get("message")
        
        data=Booking_Model(full_Name=name, phone_Number=phone,
                           email_Id=email,car_Model=car_model, 
                           service=service,date_time=date,message=message)
        data.save()
        
        
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
     if request.POST.get('num1')=="":
         return render(request,"18_EvenAndOdd.html",{"error":True})
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
    data=""
    if request.method=="POST":
        n1=int(request.POST.get('sub1'))
        n2=int(request.POST.get('sub2'))
        n3=int(request.POST.get('sub3'))
        n4=int(request.POST.get('sub4'))
        n5=int(request.POST.get('sub5'))
        total=n1+n2+n3+n4+n5
        percentage=(total/500)*100
        
        if percentage>=60:
            final="FIRST DIV"
        elif percentage>=48:
            final="SECOND DIV"
        elif percentage>=35:
            final="THIRD DIV"
        data={
            'final':final,
            'percentage':percentage,
            'total':total
             
         }  
        return render(request,"19_Marksheet.html",data)  
                
    return render(request,"19_Marksheet.html") 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
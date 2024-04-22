from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from manager.models import category
from register.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
def home(request):
      b = category.objects.all()
      return render(request,"home.html",{"categories":b})

def user_signup(request):
    if request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        if CustomUser.objects.filter(username=username) or CustomUser.objects.filter(email=email):
           messages.warning(request,"Account already exist, please Login to continue")
           return render(request,'user_login.html')
        else:
            password=request.POST['password']
            phone_no=request.POST['phone_no']
            address=request.POST['address']
            state=request.POST['state']
            pin_code=request.POST['pin_code']
            gender=request.POST['gender']
            profile_pic=request.FILES.get('profile_pic',None)
            error=[]
            if(len(username)<3):
                error.append(1)
                messages.warning(request,"Username Field must be greater than 3 character.")
            if(len(password)<5):
                error.append(1)
                messages.warning(request,"Password Field must be greater than 5 character.")
            if(len(email)==0):
                error.append(1)
                messages.warning(request,"Email field can't be empty")
            if(len(phone_no)!=10):
                error.append(1)
                messages.warning(request,"Valid Phone number is a 10 digit-integer.")
            if(len(error)==0):
                customer=CustomUser.objects.create_user(email=email,username=username,password=password,phone_no=phone_no,address=address,state=state,pin_code=pin_code,profile_pic=profile_pic,gender=gender)
                customer.is_Customer=True
                customer.save()       
                messages.info(request,"Account Created Successfully, please Login to continue")
                return render(request,'user_login.html')
            else:
                return render(request,'user_signup.html')
    return render(request,'user_signup.html')
def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user and user.is_Customer==True:
            login(request,user)
            return redirect('customer:user_home')
        else:
            messages.warning(request,"Username or password is incorrect")
            return render(request,'user_login.html')
      
    return render(request,'user_login.html')
def manager_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user and user. is_RoomManager==True:
            login(request,user)
            return redirect('manager:manager_home')
        else:
            messages.warning(request,"Username or password is incorrect")
            return render(request,'manager_login.html')
      
    return render(request,'manager_login.html')
  
def manager_signup(request):
    if request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        if CustomUser.objects.filter(username=username,) or CustomUser.objects.filter(email=email):
           messages.warning(request,"Account already exist, please Login to continue")
           return render(request,'manager_login.html')
        else:
            password=request.POST['password']
            phone_no=request.POST['phone_no']
            address=request.POST['address']
            gender=request.POST['gender']
            state=request.POST['state']
            pin_code=request.POST['pin_code']
            profile_pic=request.FILES.get('profile_pic',None)
            error=[]
            if(len(username)<3):
                error.append(1)
                messages.warning(request,"Username Field must be greater than 3 character.")
            if(len(password)<5):
                error.append(1)
                messages.warning(request,"Password Field must be greater than 5 character.")
            if(len(email)==0):
                error.append(1)
                messages.warning(request,"Email field can't be empty")
            if(len(phone_no)!=10):
                error.append(1)
                messages.warning(request,"Valid Phone number is a 10 digit-integer.")
            if(len(error)==0):
               
                manager=CustomUser.objects.create_user(email=email,username=username,password= password,phone_no=phone_no,profile_pic=profile_pic,gender=gender,address=address,state=state,pin_code=pin_code)
                manager.is_RoomManager=True
                manager.save()       
                messages.info(request,"Account Created Successfully, please Login to continue")
                return render(request,'manager_login.html')
            else:
                return render(request,'manager_signup.html')
    return render(request,'manager_signup.html')
@login_required
def user_logout(request):
    logout(request)
    return home(request)
# Create your views here.

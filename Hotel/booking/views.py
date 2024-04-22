from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from booking.models import Rooms,Booking,Contact
from django.contrib import messages
from register.models import CustomUser
from customer.models import paybook,order

def book(request):
    if request.method=="POST":
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            request.session['start_date']=start_date
            request.session['end_date']=end_date
            start_date=dt.datetime.strptime(start_date,"%Y-%m-%d").date()
            end_date=dt.datetime.strptime(end_date, "%Y-%m-%d").date()
            no_of_days=(end_date-start_date).days
            request.session['no_of_days']=no_of_days
            
            data=Rooms.objects.filter(is_available=True,end_date__gte=end_date,start_date__lte=start_date)
            return render(request,'book.html',{'data':data})
      
    return render(request,"user_home.html")
def contact(request):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        error=[]
        if(len(username)<3):
            error.append(1)
            messages.warning(request,"Username Field must be greater than 3 character.")
        if(len(email)==0):
            error.append(1)
            messages.warning(request,"Email field can't be empty")
        if(len(message)==0):
            error.append(1)
            messages.warning(request,"Message field can't be empty")    
        if(len(error)==0):
            data=Contact.objects.create(name=username,email=email,message=message)
            data.save()
            messages.info(request,"Thank you for contacting us.")
        else:
            return render(request,"contact.html")
    return render(request,"contact.html")
@login_required
def book_now(request,p):
    user=request.user
    if user.is_Customer==True:
        no_of_days=request.session['no_of_days']
        data=Rooms.objects.get(id=p)
        request.session['room_no']=data.room_no
        bill=int(no_of_days)*(data.price)
        request.session['bill']=bill
        start_date=request.session['start_date']
        end_date=request.session['end_date']
        return render(request,"book_now.html",{'data':data,'no_of_days':no_of_days,'bill':bill,"start":start_date,"end":end_date})
    else:
        return redirect('manager:manager_dashboard')
         
@login_required
def confirm_book(request):
    # username=request.session['username']
    # user_id=CustomUser.objects.get(username=username)
    # room_no=request.session['room_no']
    # room=Rooms.objects.get(room_no=room_no)
    u=request.user
    user_id=CustomUser.objects.get(username=u)
    room_no=request.session['room_no']
    room=Rooms.objects.get(room_no=room_no)
    bill=request.session['bill']
    start_date=request.session['start_date']
    end_date=request.session['end_date']
    book=Booking.objects.create(room_no=room,user_id=user_id,start_day=start_date,end_day=end_date,amount=bill)
    book.save()
    room.is_available=False
    room.save()
    pb=paybook.objects.create(user_id=u,pay_book=book) 
    pb.save()
    del request.session['start_date']
    del request.session['end_date']
    del request.session['bill']
    del request.session['room_no']
    messages.info(request,"Room has been successfully booked")
    return render(request,"user_home.html")

@login_required
def cancel_room(request,id):
    data=Booking.objects.get(id=id)
    room=data.room_no
    o=order.objects.filter(room_no=room)
    room.is_available=True
    room.save()
    data.delete()
    o.delete()
    messages.warning(request,"Booking Cancelled Successfully")
    return render(request,"user_home.html")

def about_us(request):
     return render(request,"about_us.html")
# Create your views here.

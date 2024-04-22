from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from register.models import CustomUser
from booking.models import Rooms,Booking
from manager.models import category
from manager.models import product
from customer.models import paybook,order
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse
@login_required
def manager_home(request):
      return render(request,"manager_home.html")
@login_required
def manager_dashboard(request):
      u=request.user
      data=CustomUser.objects.get(username=u)
      room_data=Rooms.objects.filter(manager=data)#CustomUser instance contain rooms_set,to access related objects.
  
      booked=room_data.filter(is_available=False).count()
      b = category.objects.all()
      print(booked)
      pb= paybook.objects.all()
    #   m=pb.pay_book.room_no.manager
      return render(request,"manager_dashboard.html",{"room_data":room_data,"manager":data,"booked":booked,"categories":b,"pb":pb,"u":u})
@login_required
def add_room(request):
    
      if request.method=="POST":
     
            room_no=request.POST['room_no']
            room_type=request.POST['room_type']
            price=request.POST['price']
            room_image=request.FILES.get('room_image',None)
            
            start_day=request.POST['start_day']
            end_day=request.POST['end_day']
            error=[]
            if(len(room_no)<1):
                error.append(1)
                messages.warning(request,"Room No Field must be atleast 3 digit like 100.")
            if(len(room_type)<5):
                error.append(1)
                messages.warning(request,"Select a valid Room Type.")
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please Enter Valid Price")
            
            if(len(start_day)<3):
                error.append(1)
                messages.warning(request,"Please add the starting day")
            if(len(end_day)<3):
                error.append(1)
                messages.warning(request,"Please add the ending day")
            if(not len(error)):
                  current_user=request.user
                  manager=CustomUser.objects.get(username=current_user)
                  room=Rooms.objects.create(room_no=room_no,room_type=room_type,price=price,start_date=start_day,end_date=end_day,room_image=room_image,manager=manager)
                  room.save()
                  messages.info(request,"Room Added Successfully")
                  return redirect('manager:manager_dashboard')
            else: 
                return render(request,"add_room.html") 
      return render(request,"add_room.html")
@login_required
def update_room(request,room_no):
      room=Rooms.objects.get(room_no=room_no)
      if request.method=="POST":
            u=request.user
            room=Rooms.objects.get(room_no=room_no,manager=u)
            price=request.POST['price']
            
            
            start_day=request.POST['start_day']
            end_day=request.POST['end_day']
           
            
            # error=[]
            # if(len(price)<=2):
            #     error.append(1)
            #     messages.warning(request,"Please enter correct price")
            
            # if(not len(error)):
            #       room.price=price
            if room.is_available:
                  
                  room.price=price
                  
                  room.start_date=start_day
                  room.end_date=end_day
                  room.save()
                  messages.info(request,"Room Data Updated Successfully")
                  return redirect('manager:manager_dashboard') 
            else:   
                 return render(request,"update_room.html",{"room":room})     
      return render(request,"update_room.html",{"room":room})  
@login_required
def delete_room(request,id):
    b = Rooms.objects.get(id=id)
    b.delete()
    messages.info(request,"Room Deleted Successfully")
    return render(request,"manager_home.html") 
@login_required
def add_menu(request,p):
    c = category.objects.get(name=p) 
    if request.method=="POST":
        name=request.POST['name']
        desc=request.POST['desc']
        price=request.POST['price']
        image=request.FILES.get('image',None)
        category1 = category.objects.get(name = request.POST['category1'])
        error=[]
        if(len(name)<1):
            error.append(1)
            messages.warning(request,"Enter a name.")
        if(len(desc)<3):
            error.append(1)
            messages.warning(request,"description minimum has 3 characters.")
        if(len(price)<=2):
            error.append(1)
            messages.warning(request,"Please enter price")
        if(not len(error)):
            p=product.objects.create(name=name,desc=desc,price=price,image=image,category1=category1)
            p.save()
            messages.info(request,"Menu Added Successfully")
            return render(request,"add_menu.html") 
        else: 
            return render(request,"add_menu.html")    
      
    return render(request,"add_menu.html",{"c":c})

def view_menu(request,p):
    c = category.objects.get(name=p)
    p = product.objects.filter(category1=c)
    return render(request,"view_menu.html",{"c":c,'p':p})
@login_required
def edit_menu(request,p):
    b = category.objects.all()
    pr = product.objects.get(name=p) 
    if request.method=="POST":
            # c = category.objects.get(name=p)
            pr = product.objects.get(name=p) 
            name=request.POST['name']
            price=request.POST['price']
            error=[]
            if(len(name)<=2):
                error.append(1)
                messages.warning(request,"Please enter name")
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter price")
            if(not len(error)):
                  pr.name=name
                  pr.price=price
                  pr.save()
                  messages.info(request,"Menu Updated Successfully")
                  return render(request,"edit_menu.html",{"pr":pr}) 
            else:   
                 return render(request,"edit_menu.html",{"pr":pr})   
    return render(request,"edit_menu.html",{"pr":pr,"categories":b}) 
@login_required
def delete_menu(request,p):
    # c = category.objects.get(name=p)
    
    pr = product.objects.filter(name=p) 
    pr.delete()
    messages.info(request,"Menu Deleted Successfully")
    return render(request,"manager_home.html") 
@login_required
def orderview(request,room_no):
    room=Rooms.objects.get(room_no=room_no)
    o=order.objects.filter(room_no=room)
    return render(request,'orderview.html',{'o':o})
   
    
# def allcategories(request):
#     b = category.objects.all()
#     return render(request,"category.html",{"categories":b})
   
# def delete_room(request,id):
#     room=Rooms.objects.get(id=id)
#     u=request.user
#     manager=room.manager.username
#     if manager==u:
#         room.delete()
#         messages.info(request,"Room Cancelled Successfully")
#         return redirect('manager:manager_dashboard') 
#     else:
#         messages.warning(request,"Room can not be cancelled")
#         return render(request,"manager_dashboard.html") 
     

        
  
    
                


# Create your views here.
# Create your views here.

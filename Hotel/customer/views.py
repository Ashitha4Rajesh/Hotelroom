from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from register.models import CustomUser
from booking.models import Booking,Rooms
from manager.models import category,product
from customer.models import order,account,paybook,payorder
import datetime
from datetime import date
from decimal import Decimal
from django.contrib import messages
@login_required
def customer_dashboard(request):
      u=request.user
      data=CustomUser.objects.get(username=u)
      booking_data=Booking.objects.filter(user_id=data)
      counts=booking_data.filter(end_day__lt=datetime.datetime.now()).count()
      today = datetime.datetime.now()
      available=booking_data.filter(end_day__gt=datetime.datetime.now()).count()
      b = category.objects.all()
      return render(request,"customer_dashboard.html",{"data":booking_data,"count":counts,"available":available,"categories":b,"today":today})
 
      
@login_required
def user_home(request):
      return render(request,"user_home.html")
@login_required
def order_menu(request,p):
      p = product.objects.get(name=p) 
      if request.method=="POST":
            try:      
            
                  quantity=request.POST['quantity']
            
                  amount = p.price * Decimal(quantity)
           
                  room1 = Rooms.objects.get(room_no= request.POST['room_no'])
            
            

                  user=request.user
                  book = Booking.objects.get(user_id=user,room_no=room1)
                  error=[]
                  if(len(quantity)<1):
                        error.append(1)
                        messages.warning(request,"Enter the quantity")
                  if(len('room_no')<1):
                        error.append(1)
                        messages.warning(request,"Please enter the room no")
            
                  if (not len(error)):
                        if(book and date.today()<book.start_day):
                              order1 = order.objects.create(product1=p,user_id=user,quantity=quantity,room_no=room1,amount=amount)
                              order1.save()
                              pr=payorder.objects.create(user_id=user,pay_order=order1) 
                              pr.save()
                              messages.info(request,"Menu Ordered Successfully")
                              return render(request,"order_menu.html")
            except:
                        
                              messages.info(request,"Enter correct room number")
                              return render(request,"order_menu.html")
      return render(request,"order_menu.html")
@login_required
def view_order(request):
    u=request.user
    o=order.objects.filter(user_id=u)
    return render(request,'view_orders.html',{'o':o})
 
@login_required
def payment(request,id):
      u=request.user
      bo=Booking.objects.get(user_id=u,id=id)
      room=bo.room_no.room_no
      request.session['id']=id
      t= bo.amount
      r=Rooms.objects.get(room_no=room)
      c=order.objects.filter(user_id=u,room_no=r)
     
      total=0
      for i in c:
          total+=i.quantity*i.product1.price
   
      total1=total+Decimal(t)
      deposit=total1//3
      balance=total1-deposit         
      # c = payorder.objects.filter(user_id=u)
      b = paybook.objects.get(user_id=u,pay_book=bo)
      if not b:
            messages.info(request,"No Order For Room")
            return render(request,"payment.html",{'c':c,'total':total,'b':b,'t':t,'total1':total1,'deposit':deposit,'balance':balance})
      if not c:
            messages.info(request,"No Order For Food")
            return render(request,"payment.html",{'c':c,'total':total,'b':b,'t':t,'total1':total1,'deposit':deposit,'balance':balance})
      return render(request,"payment.html",{'c':c,'total':total,'b':b,'t':t,'total1':total1,'deposit':deposit,'balance':balance})
def orderform(request):
    if(request.method=="POST"):
        a = request.POST["a"]
        p = request.POST["p"]
        n = request.POST["n"]
      
        u=request.user
       
        id=request.session['id']
        b=Booking.objects.get(user_id=u,id=id)
        room=b.room_no.room_no
        t=0
        
        t= t+b.amount
        
        r=Rooms.objects.get(room_no=room)
        c=order.objects.filter(room_no=r)
        c.phone_no=p
        c.username=n
        total=0
        for i in c:
          total+=i.quantity*i.product1.price
        total1=total+Decimal(t)
        deposit=total1//3
        acc=account.objects.get(acctnum=a)
        if acc.amount>=deposit:
            acc.amount=acc.amount-deposit
            acc.save()
            msg="Booked successfully"
            b=paybook.objects.get(user_id=u,pay_book=b)
            b.paid=True
            b.save()
            po=payorder.objects.filter(user_id=u)
            for i in po:
                 po.delete()
            return render(request,'orderdetail.html',{'msg':msg})
            
        else:
            msg="insufficient balance to place a Booking"
            return render(request,'orderdetail.html',{'msg':msg})
    return render(request,'orderform.html')    
# @login_required
# def delete_order(request,id):
#     b = order.objects.get(id=id)
#     b.delete()
#     messages.info(request,"Order Cancelled Successfully")
#     return render(request,"user_home.html") 
     
# Create your views here.


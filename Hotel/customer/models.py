from django.db import models
from manager.models import product
from booking.models import Rooms,Booking
from register.models import CustomUser
class order(models.Model):
    product1 = models.ForeignKey(product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    room_no=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    amount=models.FloatField()
    date_ordered=models.DateTimeField(auto_now_add=True)
    def subtotal(self):
        return self.product1.price * self.quantity
class account(models.Model):
    acctnum=models.CharField(max_length=20)
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()
    def __str__(self):
        return self.accttype
class payorder(models.Model):
    pay_order=models.ForeignKey(order, on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
 
class paybook(models.Model):
    pay_book=models.ForeignKey(Booking, on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    paid=models.BooleanField(default=False)
   

   
   
   


# Create your models here.

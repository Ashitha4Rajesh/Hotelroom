from django.db import models
from datetime import date
from register.models import CustomUser
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)
    def __str__(self):
        return self.name
class Rooms(models.Model):
    room_type = ( 
    ("Single Room", "Single Room"), 
    ("Double Room", "Double Room"),
    ("Deluxe Room","Deluxe Room"),    
    ("Super Deluxe Room","Super Deluxe Room"),    
    ) 
    manager=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room_no=models.CharField(max_length=5)
    room_type=models.CharField(max_length=50,choices = room_type)
    is_available=models.BooleanField(default=True)
    price=models.FloatField()
    end_date=models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    room_image=models.ImageField(upload_to="media",blank=True,null=True)
    def __str__(self):
        return self.room_type

class Booking(models.Model):
    room_no=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_day=models.DateField(auto_now=False, auto_now_add=False)
    end_day=models.DateField(auto_now=False, auto_now_add=False)
    amount=models.FloatField()
    booked_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    @property
    def is_past_due(self):
        return date.today()<self.start_day
    @property
    def is_past(self):
        return date.today()<self.start_day or date.today()>self.end_day
  

# Create your models here.

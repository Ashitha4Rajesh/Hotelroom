from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    gender = ( 
    ("M", "Male"), 
    ("F", "Female"),
    ("O","Others"),    
    ) 
    gender = models.CharField(max_length=50,choices = gender)
    profile_pic=models.ImageField(upload_to="media",blank=True,null=True)
    phone_no=models.CharField(max_length=50)
    address=models.TextField()
    state=models.CharField(max_length=30,blank=True,null=True)
    pin_code=models.IntegerField(blank=True,null=True)
    is_RoomManager = models.BooleanField(default=False)
    is_Customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.username

  
  



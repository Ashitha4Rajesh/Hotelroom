from django.contrib import admin
from register.models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','phone_no','address','is_RoomManager','is_Customer','email')
    list_per_page = 3
admin.site.register(CustomUser,CustomUserAdmin)
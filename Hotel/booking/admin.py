from django.contrib import admin
from booking.models import Contact
from booking.models import Rooms
from booking.models import Booking
# Register your models here.
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_no','room_type','manager','room_image', 'start_date','end_date','price')
    list_editable = ('manager','room_image',)
    list_per_page = 3
    search_fields = ('room_type',)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room_no','user_id', 'start_day','end_day','amount')
    list_per_page = 3
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
admin.site.register(Contact,ContactAdmin)
admin.site.register(Rooms,RoomsAdmin)
admin.site.register(Booking,BookingAdmin)
# Register your models here.

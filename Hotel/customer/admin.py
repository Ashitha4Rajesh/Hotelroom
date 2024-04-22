from django.contrib import admin
from customer.models import order
from customer.models import account
from customer.models import paybook
from customer.models import payorder
admin.site.register(order)
admin.site.register(account)
admin.site.register(paybook)
admin.site.register(payorder)
# Register your models here.

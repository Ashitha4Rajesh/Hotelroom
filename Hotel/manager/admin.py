from django.contrib import admin
from manager.models import category,product
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name','desc','image')
    list_editable = ('desc','image',)
class productAdmin(admin.ModelAdmin):
    list_display = ('category1','name','desc','image','price')
    list_editable = ('price','image','name',)
    list_per_page = 3
admin.site.register(category,categoryAdmin)
admin.site.register(product,productAdmin)

# Register your models here.

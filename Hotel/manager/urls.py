"""
URL configuration for Hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manager import views
from django.conf.urls.static import static
app_name="manager"
urlpatterns = [
   path('manager_home',views.manager_home,name='manager_home'),
   path('manager_dashboard',views.manager_dashboard,name='manager_dashboard'),
   path('user/add-room/new/',views.add_room,name='add_room'),
   path('add_menu/<p>',views.add_menu,name='add_menu'),
   path('view_menu/<p>',views.view_menu,name='view_menu'),
    path('orderview/<int:room_no>',views.orderview,name='orderview'),
   path('edit_menu/<p>',views.edit_menu,name='edit_menu'),
   path('delete_menu/<str:p>',views.delete_menu,name='delete_menu'),
   path('update_room/<int:room_no>',views.update_room,name='update_room'),
   path('delete_room/<str:id>',views.delete_room,name='delete_room'),
#    path("category",views.allcategories,name='allcategories'),
   
]

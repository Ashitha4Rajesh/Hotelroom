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
from customer import views
from django.conf.urls.static import static
app_name="customer"
urlpatterns = [
     
      path('customer_dashboard',views.customer_dashboard,name='customer_dashboard'),
      path('user_home',views.user_home,name='user_home'),
      path('order_menu/<p>',views.order_menu,name='order_menu'),
      path('view_order',views.view_order,name='view_order'),
      path('payment/<str:id>',views.payment,name='payment'),
      path('orderform',views.orderform,name='orderform'),
    #   path('delete_order/<str:id>',views.delete_order,name='delete_order'),
     
]

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
from booking import views
from django.conf.urls.static import static
app_name="booking"
urlpatterns = [
       
    path('book/',views.book,name='book'),
    path('book_now/<int:p>',views.book_now,name='book_now'),
    path('confirm-now-booking',views.confirm_book,name='confirm_book'),
    path('cancel-room/<int:id>',views.cancel_room,name='cancel_room'),
    path('contact-us',views.contact,name='contact_us'),
     path('user/login?next=/about_us',views.about_us,name='about_us'),
]

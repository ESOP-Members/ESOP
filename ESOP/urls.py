"""ESOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

from django.contrib import admin
from django.urls import path
from esop import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),

    path('register/',user_views.register,name='register'),
    path('base/',user_views.base,name='base'),
    path('login/',user_views.login_user,name='login_user'),
    path('index/',user_views.index,name='index'),
    #path('index/barber',user_views.barber,name='')
    path('about/', user_views.barber, name='barber'),
    path('esop/',user_views.laundary,name='laundary'),
    path('erick/',user_views.erick,name='erick'),
    path('profile/',user_views.profile,name='profile'),
    path('logout/', user_views.logout_user, name='logout_user'),
    path('mbs/', user_views.mbs, name='mbs'),
    path('mail_pay/', user_views.mail_pay, name='mail_pay'),
    path('payment/', user_views.payment, name='payment'),
]

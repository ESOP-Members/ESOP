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
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from services import views as user_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),


    path('register/',user_views.register,name='register'),
    
    path('login/',user_views.login_user,name='login_user'),
    path('index/',user_views.index,name='index'),
    

    path('about/', user_views.barber, name='barber'),
    path('services/',user_views.laundary,name='laundary'),
    path('erick/',user_views.erick,name='erick'),
    path('logout/', user_views.logout_user, name='logout_user'),
    url(r'^profile/',user_views.profile,name='profile'),
    path('ajax/', user_views.validate_username, name='validate_username'),
    path('ajax/validate/username/', user_views.reg_username, name='reg_username'),
    path('ajax/validate/email/', user_views.reg_email, name='reg_email'),
    path('ajax/validate/password/', user_views.reg_password, name='reg_password'),
    path('ajax/validate/submit/', user_views.reg_submit, name='reg_submit'),
    path('update_profile',user_views.update_profile,name = 'update_profile'),
    path('meat_eat/',user_views.meat,name='meat'),
    path('mbs/',user_views.mbs,name='mbs'),
    path('payment/',user_views.payment,name = 'payment'),
    path('mail_pay/',user_views.mail_pay,name ='mail_pay'),
    path('get_items/',user_views.get_items,name ='get_items'),
    path('change_pic/',user_views.change_pic,name ='change_pic'),

]

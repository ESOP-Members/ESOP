from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from .forms import *
from .models import UserProfile, Customer, Seller, User
from django.http import *

flag = 0
# Create your views here.
def register(request):

    form = UserForm(request.POST or None)
    #return render(request, 'esop/register.html', {'error_message': form})

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        #password2 = form.cleaned_data['password2']
        if password == password:

            email = form.cleaned_data['email']
            user.set_password(password)
            user.username = username
            user.email = email
            user.is_active = True
            user.save()
            user = authenticate(username = username, password = password)
        else :
            return render(request, 'esop/register.html', {'error_message' : 'Passwords not Correct!!'})


        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'esop/index.html')
    else:
        context = {
            "form" : form,
        }


        return render(request, 'esop/register.html', context)

def logout_user(request):
    try:
        del request.session['username']
    except:
        pass

    return render(request, 'music/login.html')


def base(request):
    if request.user.is_authenticated :
        return render(request, 'esop/base.html')
    else:
        return render(request,'esop/login.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['username']=username
                u = request.user
                #return render(request, 'esop/login.html', {'error_message': u})
                user_role = UserProfile.objects.filter(id = u.id)
                return render(request, 'esop/index.html', {'user_role': user_role})
            else:
                return render(request,'esop/login.html', {'error_message': 'Your account has been disabled'})

        else:
            return render(request, 'esop/login.html', {'error_message': 'Invalid login'})
    return render(request, 'esop/login.html')




def index(request):
    if request.session.has_key('username'):
        return render(request,'esop/index.html')
    else:
        return HttpResponseRedirect('/login')

def barber(request):

    return render(request,'esop/about.html')


def laundary(request):
    return render(request, 'esop/services.html')

def erick(request):
    return render(request, 'esop/erick.html')

def profile(request):
    form = CustomerForm(request.POST)
    # print (form.cleaned_data['first_name's])
    print ("HI1")
    if form.is_valid():
        print ("HI")
        user = form.save(commit=False)
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['mobile']
        email = form.cleaned_data['email']
        location = form.cleaned_data['location']
        # password = form.cleaned_data['password']

        user.first_name = first_name
        user.last_name = last_name
        user.mobile = phone
        user.address = location
        user.email = email

        user.save()

    else:
        context = {
            "form" : form,
        }




    return render(request, 'esop/profile.html')

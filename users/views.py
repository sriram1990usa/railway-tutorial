from django.db.models import Max
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *
from home.models import *
import json


def logout_request(request):
    print('ln 16 from users.views.logout_request')
    auth.logout(request)
    return render(request, 'users/logout.html')
    #return redirect("http://127.0.0.1:8000/")

@csrf_exempt
def login_request(request):
    print('ln 23 from users.views.login_request')
    template = loader.get_template('users/login.html')
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    print('ln 36 users.views.login_request user is active')
                    login(request, user)
                    return redirect('/', request)

            return HttpResponse('<h1>Invalid Credentials</h1>')
        return HttpResponse('<h1>invalid Data</h1>')
    else:
        return HttpResponse(template.render({}, request))
'''
@csrf_exempt
def register(request):
    print('ln 46 from users.views.register')
    #template = loader.get_template('users/Register.html')
    if request.method == 'POST':
        print('ln 49 from users.views.register.post')
        form = UserReg(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            data = form.cleaned_data
            usr = data['username']
            pas = data['password']
            eml = data['email']
            nmb = data['number']
            a = Members()
            a.username = usr
            a.password = pas
            a.email = eml
            a.number = nmb
            a.save()
            user.set_password(pas)
            user.save()
            user = authenticate(username=usr, password=pas)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home/', request)
                    # return render(request, 'users/register.html')
            else:
                messages.error(request, ('user is none'))

            return HttpResponse('<h1>VALID</h1>')
        else:
            messages.error(request,('form is invalid'))

        #return HttpResponse(template.render({'form': form}, request))
        return render(request, 'users/register.html')
    else:
        print('ln 81 from users.views.register.notPost')
        return render(request, 'users/register.html')
        # return HttpResponse(template.render({}, request))
'''

@csrf_exempt
def register(request):
    print('ln 89 from users.views.register')
    form=UserReg()
    if request.method == 'POST':
        print('ln 92 from users.views.register.post')
        form = UserReg(request.POST)
        # form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        print('ln 81 from users.views.register.notPost')
        form = UserReg(request.POST)
    form = UserReg()
    return render(request, 'users/register.html', {'form': form})

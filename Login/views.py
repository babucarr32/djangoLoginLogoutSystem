from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == "POST":
        userLogin = auth.authenticate(username = request.POST['username'], password = request.POST['password']) 
        if userLogin is not None:
            auth.login(request, userLogin)
            return redirect('/')
        else:
            return redirect('SIGNUP')
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
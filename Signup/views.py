from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signout(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                userSignup = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {"UserExists": "Username has already been taken"})
            except User.DoesNotExist:
                userSignup = User.objects.create_user(request.POST['username'], request.POST['password1'])
                auth.login(request, userSignup)
                return redirect('/')
        else:
            return render(request, 'signup.html', {"passwordUnmatched": "Password does not match"})
    else:
        return render(request, 'signup.html')
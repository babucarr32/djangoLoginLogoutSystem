from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def homepage(request):
    return render(request, 'index.html')
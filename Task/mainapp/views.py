# core/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User

def index_view(request):
    return render(request,'index.html')

def login_view(request):
    return render(request,'Task.html')


def task_view(request):
    return render(request, 'Task.html')


def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('registration')

        # Hash the password before saving
        hashed_password = make_password(password)
        user = User(username=username, password=hashed_password)
        user.save()

        messages.success(request, 'Registration successful. You can now login.')
        return redirect('login')

    return render(request, 'registration.html')



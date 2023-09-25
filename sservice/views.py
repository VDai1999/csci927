from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.db import models

from .models import Student

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']

        # Check if username exists
        if Student.objects.filter(user_name=username).exists():
            # Check if password matchs
            if Student.objects.filter(password=password).exits():
                return redirect('dashboard')  # Redirect to the dashboard upon successful login
        
        return render(request, 'login.html')
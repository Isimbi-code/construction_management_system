from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse 
from django.views.generic import TemplateView
from django.views.decorators.http import require_GET
from .forms import UserRegisterForm





class HomeView(TemplateView):
    template_name = 'authentication/home.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('login')     
        else:
            print(form.errors)
            return render(request, 'authentication/register.html', {'form': form})
    else:
        form = UserRegisterForm()  

    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'authentication/login.html',{'error':'Invalid credentials'})


    return render(request,'authentication/login.html')


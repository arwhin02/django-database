from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .forms import ProductForm, CustomUserCreation, CustomLoginForm


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-success')
    else:
        form = ProductForm()
    
    return render(request, 'addProduct.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreation()
    return render(request, 'html/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomLoginForm()
    return render(request, 'html/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'html/index.html')
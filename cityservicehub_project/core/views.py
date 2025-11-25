# core/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def forget_view(request):
    return render(request, 'forget.html')

def service_view(request):
    return render(request, 'service.html')

def service_provider_view(request):
    return render(request, 'service_provider.html')
def name():
    return "Hello"
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.Ligin_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('forget/', views.forget_view, name='forget'),
    path('services/', views.service_view, name='services'),
    path('service-provider/', views.service_provider_view, name='service_provider'),
]
"""inteb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from clients.views import clients, add_client, client_detail, add_client_staff

app_name = 'clients'

urlpatterns = [
    path('', clients,  name='clients'),
    path('add/', add_client, name='add_client'),
    path('client_detail/<int:pk>/', client_detail, name='client_detail'),
    path('add_client_staff/', add_client_staff, name='add_client_staff'),

]

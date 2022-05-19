from django.contrib import auth
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import IntebUserLoginForm


class IntebUserRegisterView(CreateView):

    template_name = 'staff/register.html'
    sucess_url = reverse_lazy('login')

class IntebUserLoginView(LoginView):
    template_name = 'staff/login.html'
    form_class = IntebUserLoginForm



    def get_success_url(self):
        return reverse_lazy('index')
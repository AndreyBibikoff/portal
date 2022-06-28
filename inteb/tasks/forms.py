import datetime

from django import forms
from django.forms import SelectDateWidget, DateTimeInput
from django.forms.utils import ErrorList

from .models import IntebUser, IntebTasks, Executors
from extras import *


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = IntebTasks
        fields = ['topic', 'text', ]


    widgets = {
        'topic': forms.TextInput(attrs={'class': 'form-input'}),
        'text': forms.Textarea(attrs={'cols': 30, 'rows': 1, }),
        # 'deadline': DateTimeInput(attrs={'type': "datetime-local"}),
    }

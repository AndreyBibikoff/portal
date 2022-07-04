import datetime

from django import forms
from django.forms import DateField, DateInput

from inteb import settings
from .models import Clients, Images, ClientsStaff, CompanyComments


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddClientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-label', 'form-control', 'col-30'


class ImgToForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['img']


class AddClientStaff(forms.ModelForm):
    class Meta:
        model = ClientsStaff
        fields = ['lastname', 'firstname', 'middlename', 'bdate', 'position', 'work_phone', 'mobile_phone',
                  'email']

    def __init__(self, *args, **kwargs):
        super(AddClientStaff, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-label', 'form-control', 'col-30'


class CompanyCommentForm(forms.ModelForm):
    class Meta:
        model = CompanyComments
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CompanyCommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-label', 'form-control', 'col-30', 'rows="3"'


class ClientStaffForm(forms.ModelForm):
    bdate = DateField(label='День рождения', input_formats=settings.DATE_FORMAT, widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ClientsStaff
        fields = '__all__'
    # def __init__(self, *args,**kwargs):
    #     super(ClientStaffForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-label', 'form-control', 'col-30', 'rows="3"'

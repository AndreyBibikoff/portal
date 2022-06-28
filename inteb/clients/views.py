from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from clients.forms import AddClientForm, ImgToForm, AddClientStaff
from clients.models import Clients, ClientsStaff, Images


# Create your views here.

def clients(request):
    title = 'ИнТеБ - Клиенты'
    all_clients = Clients.objects.all()

    context = {
        'title': title,
        'all_clients': all_clients,

    }

    return render(request, 'clients/clients.html', context)


def add_client(request):
    title = f'ИнТеБ - создание карточки клента'
    clients_form = AddClientForm

    if request.method == 'POST':
        clients_form = AddClientForm(request.POST, request.FILES)
        if clients_form.is_valid():
            clients_form.save()
            return HttpResponseRedirect(reverse('clients:clients'))

    context = {
        'title': title,
        'form': clients_form,
        'user': request.user,
    }

    return render(request, 'clients/add_client.html', context=context)


def client_detail(request, pk):
    client = get_object_or_404(Clients, pk=pk)
    title = f'ИнТеБ - Карточка клиента {client.company_name}'

    if request.method == 'POST':
        clients_form = AddClientForm(request.POST, request.FILES, instance=client)
        img = ImgToForm(request.POST, request.FILES)
        if clients_form.is_valid() and img.is_valid():
            img_form = img.save(commit=False)
            img_form.company_img = Clients.objects.get(id=pk)
            clients_form.save()
            img_form.save()
            return HttpResponseRedirect(reverse('clients:clients'))

    else:
        clients_form = AddClientForm(instance=client)
        img = ImgToForm()

    context = {
        'title': title,
        'update_form': clients_form,
        'client': client,
        'img': img,

    }

    return render(request, 'clients/client_detail.html', context=context)


def add_client_staff(request):
    title = f'ИнТеБ - Добавление клиентского сотрудника'
    client_staff_form = AddClientStaff

    if request.method == 'POST':
        client_staff_form = AddClientStaff(request.POST, request.FILES)
        if client_staff_form.is_valid():
            client_staff_form.save()
            return HttpResponseRedirect(reverse('clients:clients'))

    else:
        clients_form = AddClientForm()
        print(request.POST)

    context = {
        'title': title,
        'form': client_staff_form,
    }

    return render(request, 'clients/add_client_staff.html', context=context)

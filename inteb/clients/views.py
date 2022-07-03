from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from clients.forms import AddClientForm, ImgToForm, AddClientStaff, CompanyCommentForm, ClientStaffForm
from clients.models import Clients, ClientsStaff, Images
from django.core.cache import cache


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
        comment = CompanyCommentForm(request.POST, request.FILES)

        if clients_form.is_valid() and img.is_valid() and comment.is_valid():
            img_form = img.save(commit=False)
            comment_form = comment.save(commit=False)
            if comment_form.comment is not '':
                img_form.company_img = Clients.objects.get(id=pk)
                comment_form.company = Clients.objects.get(id=pk)
                comment_form.author = request.user
                clients_form.save()
                img_form.save()
                comment_form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                img_form.company_img = Clients.objects.get(id=pk)
                clients_form.save()
                img_form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        clients_form = AddClientForm(instance=client)
        img = ImgToForm()
        comment = CompanyCommentForm()

    context = {
        'title': title,
        'update_form': clients_form,
        'client': client,
        'img': img,
        'comment': comment,

    }

    return render(request, 'clients/client_detail.html', context=context)


def add_client_staff(request, pk):
    client = Clients.objects.get(pk=pk)
    title = f'ИнТеБ - Добавление клиентского сотрудника'

    if request.method == 'POST':
        client_staff_form = AddClientStaff(request.POST, request.FILES)
        if client_staff_form.is_valid():
            staff_form = client_staff_form.save(commit=False)
            staff_form.company = client
            staff_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        client_staff_form = AddClientStaff()
        print(request.POST)

    context = {
        'title': title,
        'form': client_staff_form,
        'client': client,

    }

    return render(request, 'clients/add_client_staff.html', context=context)


def client_staff_detail(request, pk):
    client = Clients.objects.get(pk=pk)
    staff = ClientsStaff.objects.all()
    title = f'ИнТеБ - Сотрудники клиента {client.company_name}'

    context = {
        'title': title,
        'client': client,
        'staff': staff,

    }

    return render(request, 'clients/client_staff_detail.html', context=context)


def client_staff_edit(request, pk):
    client_staff = ClientsStaff.objects.get(pk=pk)
    title = f'ИнТеБ - Карточка сотрудника {client_staff.lastname} {client_staff.firstname} {client_staff.middlename}'
    print('1')
    if request.method == 'POST':
        print('пока тут')
        clients_staff_form = ClientStaffForm(request.POST, request.FILES, instance=client_staff)
        if clients_staff_form.is_valid():
            print('ура')
            clients_staff_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print(clients_staff_form)
    else:
        clients_staff_form = ClientStaffForm(instance=client_staff)
    # print(request.POST)

    context = {
        'title': title,
        'client_staff': client_staff,
        'edit_form': clients_staff_form,
    }

    return render(request, 'clients/client_staff_edit.html', context=context)
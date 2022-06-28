from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import AddTicketForm
from .models import IntebTasks, Executors


def tasks(request):
    title = 'ИнТеБ - задачи'
    task = IntebTasks.objects.all()
    executor = Executors.objects.all()

    context = {
        'title': title,
        'task': task,
        'executor': executor,
    }

    return render(request, 'tasks/tasks.html', context=context)


def ticket(request, pk):
    title = f'ИнТеБ - задача #{pk}'
    # task = IntebTasks.objects.get(pk=pk)
    # executors = Executors.objects.get(pk=pk)

    context = {
        'title': title,
        'ticket': get_object_or_404(IntebTasks, pk=pk),

    }

    return render(request, 'tasks/ticket.html', context=context)


def add_ticket(request):
    title = f'ИнТеБ - создать задачу'
    task = IntebTasks.objects.all()
    executors = Executors.objects.all()
    ticket_form = AddTicketForm


    if request.method == 'POST':
        ticket_form = AddTicketForm(request.POST, request.FILES)
        print(type(ticket_form))
        if ticket_form.is_valid():
            ticket_form.save()
            return HttpResponseRedirect(reverse('tasks:tasks'))

        else:
            print('invalo\id')

    context = {
        'title': title,
        'ticket': task,
        'executors': executors,
        'form': ticket_form,
        'user': request.user,
    }

    return render(request, 'tasks/add_ticket.html', context=context)

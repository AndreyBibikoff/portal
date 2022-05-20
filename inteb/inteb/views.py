from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    title = 'ИнТеБ - Главная'

    context = {
        "title": title,
        'user': request.user,
    }
    return render(request, 'inteb/index.html', context=context)



def custom404(request, exception):
    return render(request, 'inteb/err.html')

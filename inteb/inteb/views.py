from django.shortcuts import render


def index(request):
    title = 'ИнТеБ - Главная'

    context = {
        "title": title
    }
    return render(request,'inteb/index.html', context=context)
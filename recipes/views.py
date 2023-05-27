from django.http import HttpResponse

from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Pedr0',
    })
    # reresponse


def contato(request):
    return HttpResponse('github and lichess')
    # return http respoturn http response


def sobre(request):
    return HttpResponse('code and stuff')

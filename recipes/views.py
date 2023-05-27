

# from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')
    # reresponse


def contato(request):
    return HttpResponse('github and lichess')
    # return http respoturn http response


def sobre(request):
    return HttpResponse('code and stuff')

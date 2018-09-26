from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeview(request):
    return HttpResponse('<h1>Dewey Decimal System Game</h1> '
                        '<p>This game will help young elementary schoolers practice '
                        'categorizing books in a library '
                        'using the Dewey Decimal System. This system, and game, will help hone their problem solving '
                        'and memory skills. </p>'
                        )


def gameview(request):
    return HttpResponse('<h1>Game Page</h1>')



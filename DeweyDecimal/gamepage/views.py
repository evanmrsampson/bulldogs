from django.shortcuts import render

# Create your views here.
def gameview(request):
    return HttpResponse('<head>'
                        '<title>Dewey Decimal System Game Page</title>'
                        '<h1>Dewey Decimal System Game</h1>'
                        '<h3><i>A Definite Work In Progress</i></h3>'
                        '</head>'
                        '<body>'
                        '<a href=""><i>what will one day be a link to the homepage</i></a>'
                        '</body>'
                        '</body>')




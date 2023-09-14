from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {
        'content':'Hej!'
    }
    return render(request, 'index.html', context=my_dict)

def users(request):
    return HttpResponse("<h1>HELLO YOU!</h1>")

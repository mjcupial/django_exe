from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>Welcome!</em><br>Go to /users to see the list of user info")

def users(request):
    return HttpResponse("<h1>HELLO YOU!</h1>")

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>Welcome!</em><br>Go to /users to see the list of user info")

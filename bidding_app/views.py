from django.shortcuts import render

from django.http import HttpResponse

from .models import Bid, User
# Create your views here.

def index(request):
    users = User.objects.raw('SELECT username FROM users')
    print(users[0])
    print("test")
    return HttpResponse("asd")

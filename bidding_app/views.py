from django.shortcuts import render

from django.http import HttpResponse

from .models import Bid, User
# Create your views here.

def index(request):
    users = User.objects.raw('select * from auth_user')
    print(users[0].username)
    return HttpResponse(users)

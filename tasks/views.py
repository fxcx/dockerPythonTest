from django.shortcuts import render
from .models import *

# Create your views here.
def index(req):
    return render(req,'index.html')


def createUser(request):
    user1= User(username="sad", password="sad")
    user2 = User(username="happendd", password="happy")
    user1.save()
    user2.save()

    info = {"INFO1": user1, "INFO2": user2}

    return render(request, 'users/created.html',info)


def getUser(req):
    user = User.objects.all()
    return render(req, 'users/get.html')


def updateUser(req):
    user = User.objects.all()
    return render(req, 'users/update.html')

def deleteUser(req):
    user = User.objects.all()
    return render(req, 'users/delete.html')
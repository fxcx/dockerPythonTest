from django.shortcuts import render
from .models import *

# Create your views here.
def index(req):
    return render(req,'home.html')

def createTask(request):
    task = Task(tittle="Tarea 1", description="Descripcion de la tarea")
    task.save()
    info = {"message": task}
    return render(request, 'tasks/createTask.html', info)



def createUser(request):
    user1= User(username="sad", password="sad")
    user2 = User(username="happendd", password="happy")
    user1.save()
    user2.save()

    info = {"INFO1": user1, "INFO2": user2}

    return render(request, 'tasks/user/createUser.html',info)


def getUser(req):
    user = User.objects.all()
    return render(req, 'user/getUser.html')
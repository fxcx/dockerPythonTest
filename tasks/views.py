from django.shortcuts import render
from .models import Task, User
from .forms import TaskForm

# Create your views here.

def addTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            return print('ffffff')
        
    return render(request,'addTasks.html')

# def CreateUser(request):
#     return render(request, 'createUser.html')


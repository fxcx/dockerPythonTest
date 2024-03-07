from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return HttpResponse("<h1> Hello, world. You're at the polls index.</h1>")

def addTask(request):
    pass
#   if request.method == 'POST':
#       form = TaskForm(request.POST)
#       if form.is_valid():
#           info_dict = form.cleaned_data

#           new_task = Task(title=info_dict['title'],
#                           description=info_dict['description'],
#                           done=info_dict['done'],
#                           created=info_dict['created'])
                         

# def addUser(request):
#    pass



# def addComment(request):
#     pass

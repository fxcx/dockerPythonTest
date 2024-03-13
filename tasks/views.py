from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.
def index(req):
    return render(req, "index.html")


def getUsers(req):
    users = User.objects.all()
    return render(req, "users/list.html", {"users":users})

def createUser(req):
    if req.method == "POST":
        form = formUser(req.POST)
        if form.is_valid():
            info = form.cleaned_data
            email = info["email"]
            result = User.objects.filter(email=email)
            if len(result) > 0:
                return render(req, "users/create.html", {"message":"ya existe el email","form": form})
            else:
                newUser = User(
                    username=info["username"],
                    password=info["password"],
                    email=info["email"],
                )
                newUser.save()
                return render(req, "users/create.html", {"message":"usuario creado"})
    else:
        form = formUser()
    return render(req, "users/create.html", {"form": form})


def updateUser(req):
    return render(req, "users/update.html")


def deleteUser(_req,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect("getusers")


# from django.http import HttpResponseRedirect
# from .forms import NameForm


# def get_name(request):
#     user= ''
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":

#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             # return HttpResponseRedirect("/thanks/")
#             user = form.cleaned_data['your_name']
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, "users/create.html", {"form": form, "user":user})

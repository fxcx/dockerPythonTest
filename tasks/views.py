from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(req):
    return render(req, "index.html")


def getUsers(req):
    users = User.objects.all()
    return render(req, "users/list.html", {"users": users})


def createUser(req):
    if req.method == "POST":
        form = formUser(req.POST)
        if form.is_valid():
            info = form.cleaned_data
            email = info["email"]
            result = User.objects.filter(email=email)
            if len(result) > 0:
                return render(
                    req,
                    "users/create.html",
                    {"message": "ya existe el email", "form": form},
                )
            else:
                newUser = User(
                    username=info["username"],
                    password=info["password"],
                    email=info["email"],
                )
                newUser.save()
                return render(req, "users/create.html", {"message": "usuario creado"})
    else:
        form = formUser()
    return render(req, "users/create.html", {"form": form})

def updateUser(req, user_id):
    if req.method == "POST":
        form = formUser(req.POST)
        if form.is_valid():
            info = form.cleaned_data
            email = info["email"]
            result = User.objects.filter(email=email)
            should_update = False
            if len(result) > 0:
                if result[0].id == user_id:
                    should_update = True
            else:
                should_update = True

            if should_update:
                user = User.objects.get(id=user_id)
                user.username = info["username"]
                user.password = info["password"]
                user.email = info["email"]
                user.save()
                return render(
                    req, "users/update.html", {"message": "usuario actualizado"}
                )
            else:
                return render(
                    req,
                    "users/update.html",
                    {"message": "ya existe el email", "form": form},
                )

    else:
        user = User.objects.get(id=user_id)
        form = formUser(
            initial={
                "username": user.username,
                "email": user.email,
            }
        )
        return render(req, "users/update.html", {"form": form})


def deleteUser(_req, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect("getusers")


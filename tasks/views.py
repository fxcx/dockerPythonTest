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


"""
email ingresado                 que tine que pasar

mismo email                     actualiza
nuevo email                     actualiza
email de otro usuario           no se actualiza

"""


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


#? Tasks


def getTasks(req):
    tasks = Task.objects.all()
    return render(req, "tasks/get.html", {"tasks": tasks})

"""
crear tarea                 que tine que pasar

misma titulo                    no se crea
nuevo tarea                     se crea
"""
def createTask(req):
    if req.method == "POST":# cuando se mande
        form = FormTask(req.POST)# lo guardo en form req.post
        if form.is_valid(): # esto lo valida
            print('esta')
            dic = form.cleaned_data # combierte dic
            titulo = dic['tittle'] # busco la clave key
            result = Task.objects.filter(tittle=titulo).exists() # exists verificar la existencia 
            if result: # si esto es verdad
             return render(req,"tasks/create.html",{"message":"ya existe","form": form})
            else:
             print('esta aca')
             form.save() # sino lo guarda
             return render(req, "tasks/create.html",{"message":"tarea creada","form": form})
    else: # renderiza el formulario igual
        form = FormTask(
            initial={
                "tittle": "tarea",
                "description": "descripcion",
                "completed": False,
            }
        )
    return render(req, "tasks/create.html", {"form": form})

"""
update tarea                 que tine que pasar

edita titulo                    se crea
titulo existente                no se crea
descripcion                     si actualiza
nuevo v cbtarea                 se crea

"""
def updateTask(req, task_id):
    if req.method == "POST":
        task = Task.objects.get(id=task_id)
        newTask = FormTask(req.POST, instance= task)
        newTask.save()
        print('esta aca')
        return render(req, "tasks/update.html", {"task":"tarea actualizada"})
    else:
        task = Task.objects.get(id=task_id)
        form = FormTask(instance=task)
        return render(req,"tasks/update.html",{"form":form})

def deleteTask(_req, task_id): # req y id de la tarea
    task = Task.objects.get(id=task_id) # metodo que busca la tarea con el id del parametro
    task.delete() # metodo que se usa para eliminar
    return redirect("lista_de_tareas") 
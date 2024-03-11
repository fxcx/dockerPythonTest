from django.urls import path
from tasks.views import *


urlpatterns = [
    path('', index),
    
    # path('getTasks/', getTasks),
    # path('createdTasks/', createTask),
    # path('updateTasks/', updateTask),
    # path('deleteTasks/', deleteTask),

    path('getUsers/', getUser),
    path('createdUsers/', createUser),
    path('updateUser/', updateUser),
    path('deleteUser/', deleteUser),


    # path('getComents/', getComents),
    # path('createdComents/', createdComents),
    # path('updateComents/', updateComent),
    # path('deleteComents/', deleteComent),

]

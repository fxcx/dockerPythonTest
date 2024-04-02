from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    
    path('getTasks/', getTasks, name='lista_de_tareas'),
    path('createTasks/', createTask,name='createTask'),
    path('updateTasks/<int:task_id>', updateTask, name='updateTask'),
    path('deleteTask/<int:task_id>', deleteTask, name='deleteTask'),

    # path('user_index/', indexUser, name='user_index'),
    path('getUsers/', getUsers, name='getusers'),
    path('createUser/', createUser, name='create'),
    path('updateUser/<int:user_id>', updateUser, name='update'),
    path('deleteUser/<int:user_id>', deleteUser, name='delete'),


    # path('getComents/', getComents),
    # path('createdComents/', createdComents),
    # path('updateComents/', updateComent),
    # path('deleteComents/', deleteComent),

]

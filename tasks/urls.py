from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    
    # path('getTasks/', getTasks),
    path('createTasks/', createTask),
    # path('updateTasks/', updateTask),
    # path('deleteTasks/', deleteTask),

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

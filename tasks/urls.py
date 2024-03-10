from django.urls import path
from tasks.views import *


urlpatterns = [
    path('', index),
    path('tasks/', createTask),
    # path('getTasks/', getTasks),

    path('users/', createUser),
    path('getUser/', getUser),
    # path('coments/', addComment),
]

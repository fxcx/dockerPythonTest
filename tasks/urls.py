from django.urls import path
from tasks.views import *


urlpatterns = [
    path('tasks/', addTask),
    path('', index),
    # path('users/', addUser),
    # path('coments/', addComment),
]

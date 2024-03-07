from django.urls import path
from .views import *


urlpatterns = [
    path('tasks/', addTask),
    path('users/', addUser),
    path('coments/', addComment),
]

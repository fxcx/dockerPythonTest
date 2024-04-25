from django.urls import path
from .views import *

app_name="tasks"

urlpatterns = [
    path('', index),
    
    # path('user_index/', indexUser, name='user_index'),
    path('get_users/', getUsers, name='getusers'),
    path('createUser/', createUser, name='create'),
    path('updateUser/<int:user_id>', updateUser, name='update'),
    path('deleteUser/<int:user_id>', deleteUser, name='delete'),

]

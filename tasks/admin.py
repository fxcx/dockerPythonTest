from django.contrib import admin
from tasks.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Task)
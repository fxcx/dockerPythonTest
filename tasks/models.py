from django.db import models

# Create your models here.
class  Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
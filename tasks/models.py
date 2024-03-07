from django.db import models

# Create your models here.
class  Task(models.Model):
    title = models.CharField(max_length=33)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    finishedTasks = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created
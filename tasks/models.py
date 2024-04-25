from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=22)
    password = models.CharField(max_length=22)
    created = models.DateTimeField(auto_now_add=True)
    finishedTasks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username}, {self.email}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}, {self.task}, {self.text}"

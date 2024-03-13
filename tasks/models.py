from django.db import models

# # Create your models here.
# class  Task(models.Model):
#     tittle = models.CharField(max_length=33)
#     description = models.TextField(null=True, blank=True)
#     done = models.BooleanField(default=False)
#     score = models.IntegerField(default=0)
#     totals= models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=22)
    password = models.CharField(max_length=22)
    created = models.DateTimeField(auto_now_add=True)
    finishedTasks = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
# class Comment(models.Model):
#     text = models.TextField()
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.created
from django import forms

class  TaskForm(forms.forms):
    title = forms.CharField(max_length=200)
    description = forms.TextField(null=True, blank=True)
    done = forms.BooleanField(default=False)
    created = forms.DateTimeField(auto_now_add=True)

 
class UserForm(forms.forms):
    username = forms.CharField(max_length=200)
    created = forms.DateTimeField(auto_now_add=True)
    finishedTasks = forms.IntegerField(default=0)

    
class CommentForm(forms.forms):
    text = forms.TextField()
    task = forms.ForeignKey(TaskForm, on_delete=forms.CASCADE)
    user = forms.ForeignKey(UserForm, on_delete=forms.CASCADE)
    created = forms.DateTimeField(auto_now_add=True)


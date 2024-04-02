from django import forms
from django.forms import ModelForm
from tasks.models import Task


class formUser(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(max_length=30)


class FormTask(ModelForm):
    class Meta:
        model = Task
        fields = ["tittle", "description", "completed","score"]
        widgets = {
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

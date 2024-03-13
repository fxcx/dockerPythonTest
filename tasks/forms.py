from django import forms
  
class formUser(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(max_length=30)
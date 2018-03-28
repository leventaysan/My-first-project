from django import forms
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
    email=forms.EmailField()

class loginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)

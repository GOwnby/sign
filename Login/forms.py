from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='Email',  max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)

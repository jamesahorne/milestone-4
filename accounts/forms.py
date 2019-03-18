from django import forms

class UserLoginForm(forms.Form):
    ''' Login form '''

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

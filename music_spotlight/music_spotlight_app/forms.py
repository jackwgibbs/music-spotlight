from django import forms


class UserForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
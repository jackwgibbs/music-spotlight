from django import forms
from .models import *


class UserForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput)


class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class NewArtist(forms.Form):
    artistName = forms.CharField(label='Artist Name', max_length=100)


class NewAlbum(forms.Form):
    albumArtist = forms.ModelChoiceField(queryset=Artists.objects.all(), label="Artist")
    albumName = forms.CharField(label='Album Name', max_length=100)
    noSongs = forms.IntegerField(label='Number of Songs')

    class Meta:
        model = Album
        fields = ("albumName", "albumArtist", "noSongs")


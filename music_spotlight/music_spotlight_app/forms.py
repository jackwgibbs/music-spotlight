from django import forms


class UserForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class NewArtist(forms.Form):
    artistName = forms.CharField(label='ArtistName', max_length=100)


class NewAlbum(forms.Form):
    albumName = forms.CharField(label='Album Name', max_length=100)
    albumArtist = forms.CharField(label='Artist Name')
    noSongs = forms.IntegerField(label='Number of Songs')
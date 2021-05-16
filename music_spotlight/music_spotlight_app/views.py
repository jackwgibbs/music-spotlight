from django.shortcuts import render

# Create your views here.
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import *
from .models import *


def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = Users(firstName=firstName, lastName=lastName, email=email, password=password)
            user.save()

            return HttpResponseRedirect('')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserLoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = Users.objects.filter(email=email, password=password)
            if user:
                print("Yes")
                return redirect('home')
            else:
                print("No")

                return redirect('/')

    else:
        form = UserLoginForm()

    return render(request, 'index.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def newArtist(request):
    form = NewArtist(request.POST)
    if form.is_valid():
        # process the data in form.cleaned_data as required
        artistName = form.cleaned_data['artistName']

        artists = Artists.objects.all()
        print(artists[0])

        artist = Artists(artistName=artistName)
        try:
            artist.save()
        except:
            print("Duplicate")

        artists = Artists.objects.all()
        print(artists[0])

        return redirect('/showartists')

    else:
        form = NewArtist()

    return render(request, 'newartist.html', {'form': form})


def showArtists(request):
    artists = Artists.objects.all()
    print(artists[0])
    context = {'context': artists}
    return render(request, 'showartists.html', context=context)


def newAlbum(request):
    form = NewAlbum(request.POST)
    if form.is_valid():
        # process the data in form.cleaned_data as required
        albumName = form.cleaned_data['albumName']

        album = Album()
        try:
            album.save()
        except:
            print("Duplicate")

        return redirect('/')

    else:
        form = NewAlbum()

    return render(request, 'newalbum.html', {'form': form})


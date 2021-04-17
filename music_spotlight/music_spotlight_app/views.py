from django.shortcuts import render

# Create your views here.
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import *
from .models import *
from django.db import models


def index(request):
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

    return render(request, 'index.html', {'form': form})

def login(request):
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
                return redirect('login')

    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')
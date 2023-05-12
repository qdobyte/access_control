from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']

            if password == password2:
                try:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'signup.html', {'error': 'Username already exists'})

            return render(request, 'signup.html', {"form": UserCreationForm, 'error': 'Passwords did not match'})


def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        if 'username' in request.POST and 'password' in request.POST:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'signin.html', {"form": AuthenticationForm, 'error': 'Username and password did not match'})
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {"form": AuthenticationForm, 'error': 'Username and password are required'})


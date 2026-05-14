from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            messages.error(request, 'Username already exists')

            return redirect('/users/register')

        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, 'You have successfully registered')

        return redirect('/users/login')

    return render(request, 'users/register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(request, 'Login successfully')

            return redirect('/books/lab11/task1/list')

        else:

            messages.error(request, 'Invalid username or password')

            return redirect('/users/login')

    return render(request, 'users/login.html')

def user_logout(request):

    logout(request)

    return redirect('/users/login')

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginUser , logout as logoutUser
from django.contrib.auth.models import auth
from django.contrib import messages
from .form import TODOForm
from .models import TODO


def home(request):
    if request.user.is_authenticated:
        form = TODOForm()
        user = request.user
        todo = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'start.html', context={'form': form, 'todos': todo})
    return render(request, 'start.html')


def addtodo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request, 'start.html', context={'form': form})
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                loginUser(request, user)
                return redirect('/')
            else:
                # print('user is not authenticated')
                return redirect('login')
        else:

            context = {
                'form': form
            }
            return render(request, 'login.html', context=context)





def signup(request):
    if request.method == 'GET':
        # print(" we are in GET")
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'signup.html', context=context)

    if request.method == 'POST':
        # print("we are in POst")
        # print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # print("valid user")
            form.save()
            if form is not None:
                return redirect('login')
        else:
            context = {
                'form': form
            }
            return render(request, 'signup.html', context=context)


def logout(request):
    logoutUser(request)
    return redirect('home')


def deletetodo(request, id):
    TODO.objects.filter(pk = id).delete()
    return redirect('home')





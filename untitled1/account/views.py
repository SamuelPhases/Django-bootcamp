from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth



# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                context = {
                    'page_title': 'Create New Account',
                    'error': 'Username already exits'
                }
                return render(request, 'account/signup.html', context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            context = {
                'page_title': 'Create New Account',
                'error': 'Password Mismatch'
            }
            return render(request, 'account/signup.html', context)
    else:
        context = {
            'page_title': 'Create New Account'
        }
        return render(request, 'account/signup.html', context)

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            context = {
                'page_title': 'Log in to your Acoount',
                'error': 'Invalid User'
            }
            return render(request, 'account/login.html', context)
    else:
        context = {
            'page_title': 'Log in'
        }
        return render(request, 'account/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

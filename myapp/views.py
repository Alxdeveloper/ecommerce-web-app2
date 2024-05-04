from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
        else:
            messages.info(request, 'Invalid user')
            return redirect('home')
    else:
        return render(request, 'home.html')
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('home')

def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


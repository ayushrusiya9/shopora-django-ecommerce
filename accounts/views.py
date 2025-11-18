from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Profile
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login

# Create your views here.
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.warning(request, 'Email is already registered!')
            return HttpResponseRedirect(request.path_info)

        #create_user() hashes password automatically and sets username
        user_obj = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )


        messages.success(request, 'Account created successfully!')
        return HttpResponseRedirect('/account/login/')  # redirect to login page

    return render(request, 'accounts/register.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if user is None:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')

        login(request, user)   # for login 

        return redirect('home')

    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

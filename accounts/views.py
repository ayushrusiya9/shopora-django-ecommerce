from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Profile
from django.http import HttpResponseRedirect

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email,password)
        user_obj = User.objects.filter(email=email).first()
        if not user_obj:
            messages.warning(request, 'user not found')

            return HttpResponseRedirect(request.path_info)
        else:
            request.session['id'] = user_obj.id
            return redirect('home')
    return render(request, 'accounts/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_image = request.FILES.get('image')

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

        Profile.objects.create(user=user_obj, profile_image=profile_image)

        messages.success(request, 'Account created successfully!')
        return HttpResponseRedirect('/account/login/')  # redirect to login page

    return render(request, 'accounts/register.html')

def logout(request):
    request.session.flush()
    return redirect('home')
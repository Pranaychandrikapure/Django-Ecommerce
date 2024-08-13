from django.shortcuts import render
from userauths.froms import UserRegisterFrom
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings
from userauths.models import User

# User = settings.AUTH_USER_MODEL

def Register(request):
    if request.method == "POST":
        form = UserRegisterFrom(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            new_user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegisterFrom()
        
    context = {
        'form':form,
    }
    return render(request, 'userauths/sign-up.html',context)

def Login(request):
    if request.user.is_authenticated:
        messages.warning(request, f'You are already logged in')
        return redirect('core:index')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {email}!!')
                return redirect('core:index')

            else:
                messages.warning(request, f'User {email} .. Wrong credentials!!')

        except:
            messages.warning(request, f'User {email} does not exist')

        

    context = {

    }

    return render(request, 'userauths/sign-in.html',context)



def Logout(request):
    logout(request)
    messages.success(request, f'You are now logged out successfully......')
    return redirect('userauths:sign-in')

        
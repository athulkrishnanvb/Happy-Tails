from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from.forms import SignupForm


# Create your views here.

def homepage(request):
    return render(request, 'homep.html')


def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_view)

    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(homepage)
    else:
        form = AuthenticationForm()

    return render(request, 'loginp.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect(homepage)

def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)
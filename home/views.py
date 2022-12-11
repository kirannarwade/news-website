from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    if request.user.is_anonymous:
        messages.warning(request, "Please Login to Access")
        return redirect('/login_user2')
    return render(request, "home.html")

def loginUser(request):
    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect('/login_user2')



class CustomerRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register_2.html', {'form':form})


    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account Register Successfully!")
            form.save()
        return render(request, 'register_2.html', {'form':form})


@login_required(login_url='/login_user2')
def contact(request):
    return render(request, "contact.html")


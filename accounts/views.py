from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def registeration(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(firstname=firstname, lastname=lastname, username=username, email=email,
                                            password1=password1, password2=password2)
            user.save()
            print("created")
        else:
            print("password matched")

        redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    username = request.POST.get('username')
    password1 = request.POST.get('username')

    return render(request, 'login.html')

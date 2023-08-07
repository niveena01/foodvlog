from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def registeration(request):
    if request.method == "POST":
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email,
                                                password=password1)
                user.save
                print("created")
        else:
            # messages.info(request, "password not matched")
            print("password not matched")
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'login')
            context = {'user': user}
            return render(request, 'login.html', context)
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

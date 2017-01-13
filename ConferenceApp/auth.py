from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import models

def login(request):

    if request.method == "GET":
        return render(request, "ConferenceApp/auth/login.html")

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                next = ""
                if "next" in request.GET:
                    next = request.GET["next"]
                if next == None or next == "":
                    next = "/conference/"
                return redirect(next)
            else:
                return render(request, "ConferenceApp/auth/login.html", { "warning": "Your account is disabled"})
        else:
            return render(request, "ConferenceApp/auth/login.html", { "warning": "Invalid username or password"})


def logout(request):
    auth.logout(request)
    return redirect('conference:index')


def register(request):
    if request.method == "GET":
        return render(request, "ConferenceApp/auth/register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        auth.models.User.objects.create_user(username, email, password).save()
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return render(request, "ConferenceApp/auth/registered.html")

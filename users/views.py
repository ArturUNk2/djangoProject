from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
# Create your views here.


def registerview(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("http://127.0.0.1:8000/next_to_page/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def loginview(request):
    return render(request,"login.html")
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm
from django.contrib import messages



def registerview(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("products")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})



def loginview(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=email,
                password=password
            )

            if user is not None:
                login(request, user)

                # ✅ добавляем сообщение
                messages.success(request, "Успешный вход")

                # ❗ НЕ redirect
                return render(request, "login.html", {"form": LoginForm()})

            else:
                messages.error(request, "Неверный email или пароль")

    return render(request, "login.html", {"form": form})
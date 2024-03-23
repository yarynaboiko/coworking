from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  login, authenticate, logout
from django.contrib import messages


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        # messages.error(request, "some error")

    return render(
        request,
        template_name="auth_system/register.html",
        context={"form": form}
        )


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
        # messages.error(request, "some error")

    return render(
        request,
        template_name="auth_system/login.html",
        context={"form": form}
        )


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

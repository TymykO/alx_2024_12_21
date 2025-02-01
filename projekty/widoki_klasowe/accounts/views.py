
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.shortcuts import render

from .forms import CustomUserCreationForm
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect("posts:index")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.


def register(request):
    """
    Создает пользователя.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

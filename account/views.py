from django.contrib.auth import login

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accont/register.html', {'form': form})


def dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'index.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
import requests


def home(request):
    if request.user.is_authenticated:
        return redirect('pokedex')
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Try again.')
    else:
        form = RegisterForm()
    return render(request, 'pokeapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            messages.error(request, 'Invalid email.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid password.')
    return render(request, 'pokeapp/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def pokedex_view(request):  # ← THIS name must match the one in urls.py
    pokemon = None
    error = None
    if request.method == "GET" and "pokemon" in request.GET:
        name = request.GET.get("pokemon").lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon = {
                "name": data["name"],
                "image": data["sprites"]["front_default"],
                "types": ", ".join(t["type"]["name"] for t in data["types"]),
                "abilities": ", ".join(a["ability"]["name"] for a in data["abilities"]),
            }
        else:
            error = f"No Pokémon found with name: {name}"

    return render(request, "pokeapp/pokedex.html", {"pokemon": pokemon, "error": error})

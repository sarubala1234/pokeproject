from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
import requests

User = get_user_model()


def home(request):
    if request.user.is_authenticated:
        return redirect('pokedex')
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the errors.')
    else:
        form = RegisterForm()
    return render(request, 'pokeapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        print(f"Login attempt: email={email}")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Authentication failed for email:", email)
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return render(request, 'pokeapp/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def pokedex_view(request):
    pokemon = None
    error = None

    if request.method == "GET" and "pokemon" in request.GET:
        name = request.GET.get("pokemon").lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"

        try:
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
        except requests.RequestException:
            error = "Error fetching Pokémon data. Please try again."

    return render(request, "pokeapp/pokedex.html", {"pokemon": pokemon, "error": error})

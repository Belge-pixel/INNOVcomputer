from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from connexion.forms import CustomUserCreationForm as UserCreation

from django.contrib.auth import login, logout
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)   # sauvegarde après ajustements
            # forcer actif si ton modèle met is_active=False par défaut
            if hasattr(user, "is_active"):
                user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, "Compte créé avec succès !")
            return redirect('accueil')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Erreur lors de l'inscription. Vérifiez les informations.")
    else:
        form = UserCreation()
    return render(request, "connexion/inscription.html", {"form": form})

def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenue {user.username} !")
            return redirect('accueil')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, "connexion/connexion.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "Vous êtes déconnecté.")
    return redirect('login')
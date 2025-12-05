from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appel
from datetime import timedelta
import random

def appel_page(request):
    appels = Appel.objects.all().order_by('-date_appel')[:10]  # Derniers 10 appels

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'appel_sortant':
            numero = request.POST.get('numero')
            type_appel = request.POST.get('type_appel', 'audio')

            if numero:
                # Simuler un appel sortant
                appel = Appel.objects.create(
                    nom_appelant="Vous",
                    numero_appelant="Votre numéro",
                    numero_destinataire=numero,
                    statut_appel='sortant',
                    type_appel=type_appel,
                    duree_appel=timedelta(seconds=random.randint(60, 300))  # Durée aléatoire
                )
                messages.success(request, f"Appel sortant vers {numero} terminé.")
            else:
                messages.error(request, "Veuillez entrer un numéro valide.")

        elif action == 'appel_entrant':
            # Simuler un appel entrant
            appel = Appel.objects.create(
                nom_appelant="Contact inconnu",
                numero_appelant="+243810684080",
                numero_destinataire="Votre numéro",
                statut_appel='entrant',
                type_appel='audio',
                duree_appel=None  # Pas répondu
            )
            messages.info(request, "Appel entrant reçu.")

        return redirect('appel_page')

    context = {
        'appels': appels,
    }
    return render(request, 'appel/appel.html', context)

from django.shortcuts import render
from formations.models import Formation

def accueil(request):
    # Get first 6 formations for preview section
    formations = Formation.objects.all()[:6]
    context = {
        'formations': formations,
    }
    return render(request, 'accueil_/accueil.html', context)

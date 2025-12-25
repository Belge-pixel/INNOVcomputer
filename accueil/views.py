from django.shortcuts import render
from formations.models import Formation
from .models import Achievement
from a_propos.models import Mission


def accueil(request):
    # Get first 6 formations for preview section
    formations = Formation.objects.all()[:6]

    # Get missions dynamically
    missions = Mission.objects.all()

    # Totals (counts) for each achievement type
    total_client_satisfait = Achievement.objects.filter(
        achievement_type=Achievement.CLIENT_SATISFIED
    ).count()
    total_projet_realise = Achievement.objects.filter(
        achievement_type=Achievement.PROJECT_COMPLETED
    ).count()
    total_annee_experience = Achievement.objects.filter(
        achievement_type=Achievement.YEARS_EXPERIENCE
    ).count()

    context = {
        'formations': formations,
        'total_client_satisfait': total_client_satisfait,
        'total_projet_realise': total_projet_realise,
        'total_annee_experience': total_annee_experience,
        'missions': missions,
        'has_missions': missions.exists(),
    }
    return render(request, 'accueil_/accueil.html', context)

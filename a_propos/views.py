from django.shortcuts import render
from expertise.models import Expertise
from formations.models import Formation
from accueil.models import Achievement
from .models import Mission, Responsable
# Create your views here.
def about(request):
    expertises = None
    formations = None
    formations = Formation.objects.all().order_by('-id')
    expertises = Expertise.objects.all().order_by('-id')
    missions = Mission.objects.all()
    responsables = Responsable.objects.all()
    
    # Totaux dynamiques des achievements
    total_annee_experience = Achievement.objects.filter(
        achievement_type=Achievement.YEARS_EXPERIENCE
    ).first()
    total_apprenants = Achievement.objects.filter(
        achievement_type=Achievement.CLIENT_SATISFIED
    ).first()
    total_projets = Achievement.objects.filter(
        achievement_type=Achievement.PROJECT_COMPLETED
    ).first()
    total_entreprises = Achievement.objects.filter(
        achievement_type=Achievement.PARTNER_COMPANIES
    ).first()
    
    context = {
        'expertises': expertises,
        "formation_list": formations,
        'missions': missions,
        'responsables': responsables,
        'total_annee_experience': total_annee_experience.value if total_annee_experience else 0,
        'total_apprenants': total_apprenants.value if total_apprenants else 0,
        'total_projets': total_projets.value if total_projets else 0,
        'total_entreprises': total_entreprises.value if total_entreprises else 0,
        'has_missions': missions.exists(),
        'has_responsables': responsables.exists(),
        'has_achievements': Achievement.objects.exists(),
    }
    return render(request, 'a_propos/about.html', context=context)

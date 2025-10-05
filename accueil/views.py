from django.shortcuts import render
from formations.models import Formation
from expertise.models import Expertise

# Create your views here.
def accueil(request):
    
    # Récupérer les 3 premières formations
    expertises = Expertise.objects.all()
    formations = Formation.objects.all()[:4]
    context = {"formations":formations}
    
    return render(request, './accueil_/accueil.html',context=context)
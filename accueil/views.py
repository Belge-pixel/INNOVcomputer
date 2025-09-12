from django.shortcuts import render
from formations.models import Formation

# Create your views here.
def accueil(request):
    
    # Récupérer les 3 premières formations
    formations = Formation.objects.all()[:4]
    context = {"formations":formations}
    
    return render(request, './accueil_/accueil.html',context=context)
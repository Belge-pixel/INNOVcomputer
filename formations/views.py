from django.shortcuts import render
from .models import Formation

def formations(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        image = request.FILES.get('image')

        if titre and description and date_debut and date_fin:
            Formation.objects.create(
                titre=titre,
                description=description,
                date_debut=date_debut,
                date_fin=date_fin,
                image=image
            )

    all_formations = Formation.objects.all()
    return render(request, 'formations/formations.html', {'formations': all_formations})

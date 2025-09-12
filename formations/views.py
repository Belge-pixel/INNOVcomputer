from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Formation

def formations(request):
    # --- Gestion du formulaire POST ---
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        points_cles = request.POST.get('points_cles')
        image = request.FILES.get('image')

        # Debug rapide
        print("POST:", request.POST)
        print("FILES:", request.FILES)

        if titre and description and date_debut and date_fin:
            Formation.objects.create(
                titre=titre,
                description=description,
                date_debut=date_debut,
                date_fin=date_fin,
                image=image,
                points_cles=points_cles
            )
            messages.success(request, "Formation enregistrée avec succès !")
            return redirect('formations')  # redirige après POST pour éviter double soumission
        else:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")

    # --- Pagination des formations ---
    all_formations = Formation.objects.all().order_by('-id')  # dernières formations en premier
    paginator = Paginator(all_formations, 3)  # 3 formations par page

    page_number = request.GET.get('page', 1)  # récupère le numéro de page depuis l'URL ?page=
    try:
        formations_page = paginator.page(page_number)
    except PageNotAnInteger:
        formations_page = paginator.page(1)
    except EmptyPage:
        formations_page = paginator.page(paginator.num_pages)

    return render(request, 'formations/formations.html', {
        'formations_list': formations_page,
        'paginator': paginator
    })

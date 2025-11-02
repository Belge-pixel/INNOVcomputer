from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Produit
from django.contrib import messages

def produits_home(request):
    # Formulaire ajout produit pour admins
    if request.method == "POST" and request.user.is_staff:
        nom_produit = request.POST.get("nom_produit")
        description_produit = request.POST.get("description_produit")
        version_produit = request.POST.get("version_produit")
        compatibilite_produit = request.POST.get("compatibilite_produit")
        licence_produit = request.POST.get("licence_produit")
        categorie_produit = request.POST.get("categorie_produit")
        image_produit = request.FILES.get("image_produit")

        if nom_produit and description_produit:
            produit = Produit(
                nom_produit=nom_produit,
                description_produit=description_produit,
                version_produit=version_produit,
                compatibilite_produit=compatibilite_produit,
                licence_produit=licence_produit,
                categorie_produit=categorie_produit,
                image_produit=image_produit if image_produit else ""
            )
            produit.save()
            messages.success(request, "Produit ajouté avec succès !")
            return redirect("produits")
        else:
            messages.error(request, "Le nom et la description sont obligatoires.")

    # Filtrage
    categorie = request.GET.get("categorie")
    search = request.GET.get("search")
    produits = Produit.objects.all()
    if categorie:
        produits = produits.filter(categorie_produit__icontains=categorie)
    if search:
        produits = produits.filter(nom_produit__icontains=search)

    # Pagination (6 produits par page)
    paginator = Paginator(produits, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'produits/produits_home.html', {'produits': page_obj})

def produit_detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'produits/produit_detail.html', {'produit': produit})

def produit_supprimer(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    produit.delete()
    return redirect('produits')  # ou le nom de ta vue principale produits

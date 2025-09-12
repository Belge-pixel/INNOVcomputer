from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import New
from django.contrib.auth.decorators import login_required

@login_required
def blog(request):
    # --- Enregistrement d'un nouvel article ---
    if request.method == "POST":
        new_title = request.POST.get("new_title")
        new_content = request.POST.get("new_content")
        new_image = request.FILES.get("new_image")  # pour le champ image

        if new_title and new_content:  # on vérifie les champs obligatoires
            New.objects.create(
                new_title=new_title,
                new_content=new_content,
                new_image=new_image or None
            )
            return redirect("blog")  # reload pour voir l'article ajouté

    # --- Liste des articles avec pagination ---
    articles_list = New.objects.all().order_by("-new_publication_date")
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 3)  # nombre d'articles par page (modifiable)
    paginator = Paginator(articles_list, per_page)

    page_obj = paginator.get_page(page_number)

    context = {
        "articles": page_obj,
        "page_obj": page_obj,
    }
    return render(request, "blog/blog.html", context)

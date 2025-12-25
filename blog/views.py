from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import New
from .forms import NewForm


# ----------------------------------------------------------------
# 🔹 Vue détaillée : Détail d'un article
# ----------------------------------------------------------------
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import New, Comment
from .forms import NewForm

from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden,HttpResponse



# ----------------------------------------------------------------
# 🔹 Vue principale : Liste des articles publiés
# ----------------------------------------------------------------
def blog(request):
    """
    Affiche la liste paginée des articles publiés.
    Seuls les articles dont le statut est 'published' sont visibles.
    """
    news_list = (
        New.objects
        .select_related('new_author')   # optimisation de requêtes SQL
        .filter(new_status='published') # uniquement les articles publiés
        .order_by('-new_publication_date')
    )

    paginator = Paginator(news_list, 6)  # 6 articles par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_articles': news_list.count(),
        'page_title': "Actualités publiées",
    }

    return render(request, 'blog/blog.html', context)



@login_required(login_url='login')
def blog_detail(request, pk):
    """
    Affiche les détails d'un article spécifique,
    ainsi que ses commentaires et articles similaires.
    """
    new = get_object_or_404(
        New.objects.select_related('new_author'),
        pk=pk,
        new_status='published'
    )

    # Tags séparés par virgule → convertis en liste
    tags = [tag.strip() for tag in new.new_tags.split(',')] if new.new_tags else []

    # Commentaires liés à cet article
    comments = new.comments.select_related('author').all()

    # Articles similaires
    related_posts = (
        New.objects
        .filter(new_category=new.new_category, new_status='published')
        .exclude(pk=pk)[:3]
    )

    # Gestion du formulaire de commentaire
    if request.method == 'POST':
        content = request.POST.get('comment_content')
        if content and request.user.is_authenticated:
            Comment.objects.create(
                new=new,
                author=request.user,
                comment_content=content
            )
            return redirect('blog_detail', pk=new.pk)

    context = {
        'new': new,
        'tags': tags,
        'comments': comments,
        'related_posts': related_posts,
        'now': timezone.now(),
        'page_title': f"{new.new_title} | Mon Blog",
    }

    return render(request, 'blog/blog_detail.html', context)

@login_required(login_url='login')
def supprimer_new(request, pk):
    """
    Supprime un article de blog si l'utilisateur est l'auteur ou staff.
    Gère les requêtes HTMX pour suppression sans rechargement.
    """
    new = get_object_or_404(New, pk=pk)

    if request.user != new.new_author and not request.user.is_staff:
        if request.headers.get("Hx-Request"):
            return HttpResponseForbidden("Vous n'avez pas la permission.")
        return HttpResponseForbidden("Vous n'avez pas la permission de supprimer cet article.")

    if request.method == 'POST':
        new.delete()
        if request.headers.get("Hx-Request"):
            return HttpResponse("")  # HTMX supprimera l'élément du DOM
        messages.success(request, "L'article a été supprimé avec succès.")
        return redirect('blog')

    context = {
        'new': new,
        'page_title': "Confirmer la suppression",
    }
    return render(request, 'blog/blog_confirm_delete.html', context)

@login_required(login_url='login')
def blog_form(request):
    """
    Permet aux utilisateurs connectés de créer un nouvel article.
    """
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.new_author = request.user
            new_post.new_publication_date = timezone.now()
            new_post.save()

            messages.success(request, " Votre article a été publié avec succès !")
            return redirect('blog_detail', pk=new_post.pk)
        else:
            messages.error(request, "Veuillez corriger les erreurs du formulaire.")
    else:
        form = NewForm()

    context = {
        'form': form,
        'page_title': "Nouvel Article",
    }

    return render(request, 'blog/blog_form.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import New  
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import NewForm

def blog(request):
    news_list = New.objects.all().order_by('-new_publication_date')
    paginator = Paginator(news_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'page_obj': page_obj})  

def blog_detail(request, pk):
    new = get_object_or_404(New, pk=pk)
    return render(request, 'blog/blog_detail.html', {'new': new})

def blog_form(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = NewForm()
    return render(request, 'blog/blog_form.html', {'form': form})
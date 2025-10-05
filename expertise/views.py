# views.py
from django.shortcuts import render
from .models import Expertise
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpertiseForm

def expertise_list(request):
    """
    Affiche la liste de toutes les expertises.
    """
    expertises = Expertise.objects.all() 
    return render(request, 'expertise/expertise.html', {'expertises': expertises})


def expertise_create(request):
    if request.method == 'POST':
        form = ExpertiseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('expertise')  
    else:
        form = ExpertiseForm()
    return render(request, 'expertise/expertise_form.html', {'form': form})

def expertise_update(request, pk):
    expertise = get_object_or_404(Expertise, pk=pk)
    if request.method == 'POST':
        form = ExpertiseForm(request.POST, request.FILES, instance=expertise)
        if form.is_valid():
            form.save()
            return redirect('expertise')
    else:
        form = ExpertiseForm(instance=expertise)
    return render(request, 'expertise/expertise_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Enquete

def details_enquete(request, enquete_id):
    enquete = get_object_or_404(Enquete, id=enquete_id)
    return render(request, 'enquetes/details_enquetes.html', {'enquete': enquete})

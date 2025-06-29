from django.shortcuts import render

# Create your views here.
def tresorerie(request):
    return render(request, 'tresorerie/tresorerie.html')
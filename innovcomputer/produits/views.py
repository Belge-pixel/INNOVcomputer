from django.shortcuts import render

# Create your views here.

def produits_home(request):
    return render(request,'produits/produits_home.html')
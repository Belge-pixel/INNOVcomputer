
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accueil.urls'), name='accueil'),
    path('produits/',include('produits.urls'), name='produit'),
]

from django.urls import path
from .views import produits_home, produit_detail, produit_supprimer

urlpatterns=[
    path('produits/',produits_home,name="produits"),
    path('produits/<int:pk>/', produit_detail, name='produit_detail'),
    path('produits/<int:pk>/supprimer/', produit_supprimer, name='produit_supprimer'),
]
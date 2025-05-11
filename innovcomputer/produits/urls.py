from django.urls import path
from .views import produits_home

urlpatterns=[
    path('produits/',produits_home,name="produits"),
]
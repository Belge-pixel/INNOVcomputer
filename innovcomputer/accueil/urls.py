from django.urls import path              
from accueil.views import accueil

urlpatterns = [
    path('', accueil, name='accueil'),
]

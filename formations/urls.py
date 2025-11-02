from django.urls import path
from . import views

urlpatterns = [
    path('formations/', views.formations, name='formations'),  # liste des formations
    path('formations/<int:pk>/', views.formation_detail, name='formation_detail'),
]

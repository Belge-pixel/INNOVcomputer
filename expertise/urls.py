from django.urls import path
from . import views 

urlpatterns = [
    path('expertise/', views.expertise_list, name='expertise'),
    path('expertise/new/', views.expertise_create, name='expertise_create'),
    path('expertise/<int:pk>/edit/', views.expertise_update, name='expertise_update'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('formations/', views.formations, name='formations'),
]

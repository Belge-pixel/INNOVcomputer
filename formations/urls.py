from django.urls import path
from . import views

urlpatterns = [
    path('', views.formations, name='formations'),
]

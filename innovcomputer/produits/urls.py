from django.urls import path
from . import views

urlpatterns=[
    path('',views.produits_home,name="produits")
]
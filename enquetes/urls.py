from django.urls import path
from . import views

urlpatterns = [
    path('<int:enquete_id>/', views.details_enquete, name='details_enquete'),
]

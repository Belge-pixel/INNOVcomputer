from django.urls import path           
from .views import tresorerie

urlpatterns = [
    path('tresorerie/', tresorerie, name='tresorerie'),
]

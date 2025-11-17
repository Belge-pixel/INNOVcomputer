from django.urls import path
from .views import appel_page

urlpatterns = [
    path('appel/', appel_page, name='appel_page'),
]

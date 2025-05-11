
from django.contrib import admin
from django.urls import path,include
import produits

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produits/',include('produits.urls'))
]

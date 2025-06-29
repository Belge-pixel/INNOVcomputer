
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accueil.urls'), name='accueil'),
    path('produits/',include('produits.urls'), name='produit'),
    path('a_propos/',include('a_propos.urls'), name='a_propos'),
    path('contact/', include('contact.urls'), name='contact'),
    path('blog/', include('blog.urls')),
    path('tresorerie/', include('tresorerie.urls')),
    path('user/', include('users.urls')),
]

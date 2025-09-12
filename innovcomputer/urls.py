
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accueil.urls'), name='accueil'),
    path('produits/',include('produits.urls'), name='produit'),
    path('a_propos/',include('a_propos.urls'), name='a_propos'),
    path('contact/', include('contact.urls'), name='contact'),
    path('blog/', include('blog.urls')),
    path('tresorerie/', include('tresorerie.urls')),
    path('user/', include('users.urls')),
    path('formations/', include('formations.urls')),
    path('connexion/', include('connexion.urls')),  
    path('enquetes/', include('enquetes.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
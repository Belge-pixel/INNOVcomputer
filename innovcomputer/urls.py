from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accueil.urls'), name='accueil'),
    path('',include('produits.urls'), name='produit'),
    path('',include('a_propos.urls'), name='a_propos'),
    path('', include('contact.urls'), name='contact'),
    path('', include('blog.urls')),
    path('', include('tresorerie.urls')),
    path('', include('users.urls')),
    path('', include('formations.urls')),
    path('', include('connexion.urls')),
    path('', include('enquetes.urls')),
    path('', include('expertise.urls')),
    path('', include('appel.urls')),
    path('', include('staff.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

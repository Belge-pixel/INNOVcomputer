from django.urls import path
from .views import blog, blog_detail, blog_form, supprimer_new

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('blog/new/', blog_form, name='blog_form'),
    path('blog/<int:pk>/delete/', supprimer_new, name='supprimer_new'),
]

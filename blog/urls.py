from django.urls import path
from .views import blog, blog_detail

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
]

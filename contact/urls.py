from django.urls import path
from .views import contact ,send_message            

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('send-message/', send_message, name='send_message'),
]

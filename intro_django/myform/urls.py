from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='contact-us'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success', views.contact_success_view, name='contact-success'),   
]
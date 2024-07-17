# Funza/urls.py
from django.urls import path
from . import views  # Import views from the current module

urlpatterns = [
    path('', views.home, name='home'),  # Assuming home view is defined in views.py
    path('about/', views.about_view, name='about'),
    path('classes/', views.classes_view, name='classes'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
]

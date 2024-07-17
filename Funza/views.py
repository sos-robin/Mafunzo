# Funza/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'Funza/index.html')

def about_view(request):
    return render(request, 'Funza/about.html')


def gallery_view(request):
    return render(request, 'Funza/gallery.html')

def contact_view(request):
    return render(request, 'Funza/contact.html')

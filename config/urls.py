"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import about, contact, index, our_work, services, thanks
from .views import deck_cleaning_restoration, fence_cleaning, outdoor_stain_removal, soft_wash, surface_cleaning


urlpatterns = [
  path('admin/',    admin.site.urls),
  path('',          include('apps.contact_form.urls', namespace='contact_form')),
  path('',          index,    name='index'),
  path('about/',    about,    name='about'),
  path('contact/',  contact,  name='contact'),
  path('our-work/', our_work,  name='our-work'),
  path('services/', services, name='services'),
  path('thanks/',   thanks,   name='thanks'),
  path('services/fence-cleaning/',             fence_cleaning,             name='fence-cleaning'),
  path('services/surface-cleaning/',           surface_cleaning,           name='surface-cleaning'),
  path('services/soft-wash/',                  soft_wash,                  name='soft-wash'),
  path('services/outdoor-stain-removal/',      outdoor_stain_removal,      name='outdoor-stain-removal'),
  path('services/deck-cleaning-restoration/',  deck_cleaning_restoration,  name='deck-cleaning-restoration'),
]
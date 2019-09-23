from django.shortcuts import render
from apps.contact_form.forms import CreateContactForm
from apps.uploaded_images.models import UploadedImages


form = CreateContactForm

# Home Page
def index(request):
  context = { 'form': form, }
  return render(request, 'index.html', context)

# About Page
def about(request):
  context = {}
  return render(request, 'about.html', context)

# Contact Page
def contact(request):
  context = { 'form': form, }
  return render(request, 'contact.html', context)

# Our Work
def our_work(request):

  # When someone visits our-work.html, query the database for anything in the
  # table represented by the UploadedImages model and store it in the context{}
  # dictionary, which contains key:value pairs where each value is a list of
  # objects that represent each image in a category represented by the 'key'
  from collections import defaultdict
  context = defaultdict(list)
  for img in UploadedImages.objects.all():
    context[img.Category].append({
      'Category': img.Category,
      'Before_Picture_Description': img.Before_Picture_Description,
      'Before_Picture': img.Before_Picture,
      'After_Picture_Description': img.After_Picture_Description,
      'After_Picture': img.After_Picture,
    })

  return render(request, 'our-work.html', context)

# Services Page
def services(request):
  context = {}
  return render(request, 'services.html', context)

# Thanks Page
def thanks(request):
  context = {}
  return render(request, 'thanks.html', context)

# Deck Cleaning and Restoration
def deck_cleaning_restoration(request):
  context = { 'form': form, }
  return render(request, 'deck-cleaning-restoration.html', context)

# Fence Cleaning
def fence_cleaning(request):
  context = { 'form': form, }
  return render(request, 'fence-cleaning.html', context)

# Outdoor Stain Removal
def outdoor_stain_removal(request):
  context = { 'form': form, }
  return render(request, 'outdoor-stain-removal.html', context)

# Soft Wash
def soft_wash(request):
  context = { 'form': form, }
  return render(request, 'soft-wash.html', context)

# Surface Cleaning
def surface_cleaning(request):
  context = { 'form': form, }
  return render(request, 'surface-cleaning.html', context)
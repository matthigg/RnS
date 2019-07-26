from django.shortcuts import render
from apps.contact_form.forms import CreateContactForm

# Home Page
def index(request):
  form = CreateContactForm
  context = { 'form': form, }
  return render(request, 'index.html', context)

# About Page
def about(request):
  context = {}
  return render(request, 'about.html', context)

# Services Page
def services(request):
  context = {}
  return render(request, 'services.html', context)

# Our Work Page
def our_work(request):
  context = {}
  return render(request, 'our-work.html', context)

# Contact Page
def contact(request):
  form = CreateContactForm
  context = { 'form': form, }
  return render(request, 'contact.html', context)

# Thanks Page
def thanks(request):
  context = {}
  return render(request, 'thanks.html', context)
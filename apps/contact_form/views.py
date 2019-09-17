from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateContactForm

import os
import requests

def submit(request):

  # reCAPTCHA v3
  r = requests.post(
    'https://www.google.com/recaptcha/api/siteverify', 
    params={
      'response': request.POST["g-recaptcha-response"],
      'secret': os.environ["RNS_RECAPTCHA_SECRET_KEY"],
    }
  )

  # Return 'error' message if reCAPTCHA fails
  if r.json()['success'] == False:
    messages.add_message(request, messages.INFO, 'There was an error with your request. We appologize for the inconvenience.')
    return redirect('contact')

  # Save message to database if valid
  if request.method == "POST":
    form = CreateContactForm(request.POST)
    if form.is_valid():
      form.save()

      messages.add_message(request, messages.INFO, 'Your Message Has Been Sent!')
      return redirect('thanks')

    # Django stores errors in form.errors
    else:
      context = {
        'form': form,
      }
      return render(request, 'contact.html', context)
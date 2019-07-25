from django.shortcuts import render, redirect
from .forms import CreateContactForm
from django.contrib import messages

def submit(request):
  if request.method == "POST":
    form = CreateContactForm(request.POST)
    if form.is_valid():
      form.save()

      messages.add_message(request, messages.INFO, 'Form is valid!')
      return redirect('thanks')

    # Django stores errors in form.error
    else:
      form = CreateContactForm()
    return render(request, 'contact', { 'form': form })
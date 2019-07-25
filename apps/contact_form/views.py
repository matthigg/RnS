from django.shortcuts import render
from django.http import HttpResponse

def submit(request):
  return HttpResponse("<h1>Success!</h1>")
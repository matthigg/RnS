from django.urls import path
from .views import submit

app_name = "contact"
urlpatterns = [
  path('submit/', submit, name='submit'),
]
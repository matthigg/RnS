from django.db import models

class ContactForm(models.Model):
  
  # Fix pluralization in admin panel
  class Meta:
    verbose_name_plural = "Contact Form" 
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length = 24)
  message = models.TextField()
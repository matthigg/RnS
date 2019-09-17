from django.db import models

STORIES_CHOICES = (
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4+', '4+'),
)

# Create your models here.
class ContactForm(models.Model):
  class Meta:
    verbose_name_plural = "Contact Form Submissions"
  name = models.CharField(max_length=254)
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length=24, default=None, blank=True)
  stories = models.CharField(max_length=6, choices=STORIES_CHOICES, default='1', null=True)
  # exterior = models.CharField(max_length=24, default=None, blank=True, null=True)
  # service_house_wash = models.BooleanField()
  message = models.TextField()
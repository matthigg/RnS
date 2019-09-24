from django.db import models

STORIES_CHOICES = (
  ('Not specified', 'Select number of stories (if applicable)'),
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4+', '4+'),
)

EXTERIOR_CHOICES = (
  ('Not specified', 'Select type of exterior'),
  ('Vinyl', 'Vinyl'),
  ('Wood', 'Wood'),
  ('Brick', 'Brick'),
  ('Aluminum', 'Aluminum'),
  ('Other', 'Other'),
)

# Create your models here.
class ContactForm(models.Model):
  class Meta:
    verbose_name_plural = "Contact Form Submissions"
  name = models.CharField(max_length=254)
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length=24, default=None, blank=True)
  number_of_stories = models.CharField(max_length=6, choices=STORIES_CHOICES, default='Not specified', null=True)
  type_of_exterior = models.CharField(max_length=24, choices=EXTERIOR_CHOICES, default='Not specified', blank=True, null=True)
  fence_cleaning = models.BooleanField(default=False, blank=True, null=True)
  surface_cleaning = models.BooleanField(default=False, blank=True, null=True)
  soft_wash = models.BooleanField(default=False, blank=True, null=True)
  outdoor_stain_removal = models.BooleanField(default=False, blank=True, null=True)
  deck_cleaning = models.BooleanField(default=False, blank=True, null=True)
  message = models.TextField()
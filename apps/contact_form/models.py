from django.db import models

STORIES_CHOICES = (
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4+', '4+'),
)

EXTERIOR_CHOICES = (
  ('vinyl', 'vinyl'),
  ('wood', 'wood'),
  ('brick', 'brick'),
  ('aluminum', 'aluminum'),
  ('other', 'other'),
)

# Create your models here.
class ContactForm(models.Model):
  class Meta:
    verbose_name_plural = "Contact Form Submissions"
  name = models.CharField(max_length=254)
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length=24, default=None, blank=True)
  number_of_stories = models.CharField(max_length=6, choices=STORIES_CHOICES, default='1', null=True)
  type_of_exterior = models.CharField(max_length=24, choices=EXTERIOR_CHOICES, default=None, blank=True, null=True)
  fence_cleaning = models.BooleanField(default=False, blank=True, null=True)
  surface_cleaning = models.BooleanField(default=False, blank=True, null=True)
  soft_wash = models.BooleanField(default=False, blank=True, null=True)
  outdoor_stain_removal = models.BooleanField(default=False, blank=True, null=True)
  deck_cleaning = models.BooleanField(default=False, blank=True, null=True)
  message = models.TextField()
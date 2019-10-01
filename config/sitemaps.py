from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
  priority = 0.5
  changefreq = 'daily'

  def items(self):
    # return ['index', 'about', 'contact', 'our-work', 'services', 'fence-cleaning', 'surface-cleaning', 'soft-wash', 'outdoor-stain-removal', 'deck-cleaning-restoration']
    return ['about']

  def location(self, item):
    return reverse(item)
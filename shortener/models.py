from django.urls import reverse
from django.db import models


class Link(models.Model):
    """
    Model that represents a shortened URL
    """
    slug = models.SlugField('Link name')
    url = models.URLField('Target URL')
    date_submitted = models.DateTimeField(auto_now_add=True)
    usage_count = models.PositiveIntegerField(default=0)

    @property
    def short_url(self):
        return reverse('shortener:follow', args=(self.slug,))

    def __str__(self):
        return '%s : %s' % (self.slug, self.url)

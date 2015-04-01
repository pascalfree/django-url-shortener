from django.core.urlresolvers import reverse
from django.db import models
from .baseconv import base62


class Link(models.Model):
    """
    Model that represents a shortened URL
    """
    url = models.CharField(max_length=255)
    date_submitted = models.DateTimeField(auto_now_add=True)
    usage_count = models.PositiveIntegerField(default=0)

    @property
    def short_url(self):
        return reverse('shortener.views.follow', args=(self.to_base62(),))

    def short_url_admin(self):
        return '<a href="%s" target="_blank"><b>%s</b></a>' % (self.short_url, self.short_url)
    short_url_admin.allow_tags = True

    def to_base62(self):
        return base62.from_decimal(self.id)

    def __unicode__(self):
        return  '%s : %s' % (self.to_base62(), self.url)
from django.contrib import admin
from django.contrib.sites.models import Site

from .settings import *
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    search_fields = ('url',)
    list_filter = ('date_submitted',)
    list_display = ('url', 'short_url_admin', 'usage_count', 'date_submitted')
    readonly_fields = ('usage_count',)

    def short_url_admin(self, obj):
        absolute_url = u'{p}://{d}{t}'.format(
            p=FULL_ABSOLUTE_PROTOCOL,
            d=Site.objects.get(pk=DEFAULT_SITE_ID).domain,
            t=obj.short_url,
        )
        return '<a href="%s" target="_blank"><b>%s</b></a>' % (absolute_url, absolute_url)
    short_url_admin.allow_tags = True


admin.site.register(Link, LinkAdmin)

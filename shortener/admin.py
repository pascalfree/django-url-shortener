from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'short_url_admin', 'date_submitted')
    readonly_fields = ('usage_count',)


admin.site.register(Link, LinkAdmin)
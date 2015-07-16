from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    search_fields = ('url',)
    list_filter = ('date_submitted',)
    list_display = ('url', 'short_url_admin', 'date_submitted')
    readonly_fields = ('usage_count',)

    def get_list_display(self, request):

        def full_short_url_admin(lnk):
            absolute_url = request.build_absolute_uri(lnk.short_url)
            return '<a href="%s" target="_blank"><b>%s</b></a>' % (absolute_url, absolute_url)
        full_short_url_admin.allow_tags = True

        return ('url', full_short_url_admin, 'date_submitted')


admin.site.register(Link, LinkAdmin)

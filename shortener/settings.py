from django.conf import settings


FULL_ABSOLUTE_PROTOCOL = getattr(settings, 'URL_SHORTENER_FULL_ABSOLUTE_PROTOCOL', 'http')
DEFAULT_SITE_ID = getattr(settings, 'URL_SHORTENER_DEFAULT_SITE_ID', 0)

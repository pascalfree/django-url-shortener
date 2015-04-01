from django.db.models import F
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET

from .baseconv import base62
from .models import Link


@require_GET
def follow(request, base62_id):
    """
    View which gets the link for the given base62_id value
    and redirects to it.
    """
    link = get_object_or_404(Link, id=base62.to_decimal(base62_id))
    link.usage_count = F('usage_count') + 1
    link.save()
    return HttpResponsePermanentRedirect(link.url)
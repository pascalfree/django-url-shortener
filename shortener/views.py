from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404

from .models import Link


@login_required
def follow(request, slug):
    """
    View which gets the link for the given base62_id value
    and redirects to it.
    """
    link = get_object_or_404(Link, slug=slug)
    link.usage_count = F('usage_count') + 1
    link.save()
    return HttpResponsePermanentRedirect(link.url)

import random
import string
import sys

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from django.test.client import Client, RequestFactory

from shortener.baseconv import base62, DecodingError, EncodingError
from shortener.models import Link
from testsettings import LOGIN_URL

# needed for the short_url templatetag
CUSTOM_HTTP_HOST = 'django.testserver'


class TemplateTagTestCase(TestCase):
    def setUp(self):
        self.HTTP_HOST = CUSTOM_HTTP_HOST
        self.factory = RequestFactory(HTTP_HOST=self.HTTP_HOST)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client(HTTP_HOST=CUSTOM_HTTP_HOST)

    def test_follow(self):
        """
        the follow view on a valid url
        """
        url = 'http://www.python.org/'
        link = Link.objects.create(slug='testslug', url=url)
        self.assertEqual(link.usage_count, 0)

        # try to open without logging in
        response = self.client.get(reverse('shortener:follow', kwargs={
            'slug': link.slug}))
        self.assertRedirects(response, LOGIN_URL, 400)

        # follow the short url and get a redirect
        User.objects.create_user('testuser', email='test@email.com')
        self.client.login(username='testuser')
        response = self.client.get(reverse('shortener:follow', kwargs={
            'slug': link.slug}))
        self.assertRedirects(response, url, 301, fetch_redirect_response=False)

        # re-fetch link so that we can make sure that usage_count incremented
        link = Link.objects.get(id=link.id)
        self.assertEqual(link.usage_count, 1)

    def test_follow_404(self):
        """
        follow on an unknown url should return 404
        """
        response = self.client.get(reverse('shortener:follow', kwargs={'slug': "fails"}))
        self.assertEqual(response.status_code, 404)


class LinkTestCase(TestCase):
    TESTURL = 'http://www.python.org'

    def test_create(self):
        link = Link.objects.create(url=self.TESTURL)
        self.assertEqual(link.slug, '')

    def test_unicode(self):
        """
        unicode test
        """
        url = self.TESTURL
        link = Link.objects.create(url=url)
        self.assertTrue(url in str(link))


class BaseconvTestCase(TestCase):
    def test_symmetry_positive_int(self):
        """
        symmetry for encoding/decoding values
        """
        for x in range(1000):
            random_int = random.randint(0, sys.maxsize)
            encoded_int = base62.from_decimal(random_int)
            self.assertEqual(random_int, base62.to_decimal(encoded_int))

    def test_symmetry_negative_int(self):
        """
        symmetry for negative numbers
        """
        for x in range(1000):
            random_int = random.randint(-1 * sys.maxsize - 1, 0)
            encoded_int = base62.from_decimal(random_int)
            self.assertEqual(random_int, base62.to_decimal(encoded_int))

    def test_encoding_non_int_fails(self):
        """
        calling from_decimal() on letters raises an EncodingError
        """
        self.assertRaises(EncodingError, base62.from_decimal, string.ascii_letters)

    def test_decoding_non_str_fails(self):
        """
        decoding a non-str should fail with DecodingError
        """
        self.assertRaises(DecodingError, base62.to_decimal, sys.maxsize)

    def test_illgal_character(self):
        """
        trying to encode a character that is not within base62 raises an
        EncodingError
        """
        self.assertRaises(DecodingError, base62.to_decimal, '@@@@')

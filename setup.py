from setuptools import setup, find_packages

version = __import__('shortener').get_version()

setup(
    version = version,
    name = "django-url-shortener",
    packages = find_packages(),
    package_data = {
        '': [],
        'django-url-shortener/': ['templates/*.*'],
        },
    author = "Nilesh D Kapadia",
    author_email = "Unknown",
    description = "",
    zip_safe=False,
    license = "Free",
    url = "http://nileshk.com/2009/06/02/url-shortener-web-app-using-django.html",
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        ],
    install_requires = ["Django>=1.0"],
)

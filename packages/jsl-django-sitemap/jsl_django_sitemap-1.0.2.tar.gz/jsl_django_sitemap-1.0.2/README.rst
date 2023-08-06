=====
JSL Django Sitemap
=====

JSL Django Sitemap is a Django app to which iterates over all the url patterns in your main Django project and creates a ready to use sitemap. The sitemap.xml is useful in crawlers such as Google, Bing, Yahoo.
We hope you like our app! Leave a star on our github repository. Thanks!


Quick start
-----------

1. Add "jsl_django_sitemap" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'jsl_django_sitemap',
    ]

2. Include the polls URLconf in your project urls.py like this::

    from jsl_django_sitemap.views import sitemaps

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

4. Start the development server and visit http://127.0.0.1:8000/sitemap.xml/


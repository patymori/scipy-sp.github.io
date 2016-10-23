#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SciPy-SP'
SITENAME = 'Observatório do SciPy-SP'
SITEURL = 'http://localhost:8000'


ROBOTS = 'index, follow'

# Creative Commons Licensing
CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2016
DISPLAY_PAGES_ON_MENU = False
MAIN_MENU = True


PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Materiais', ''),
    ('SciPy', 'http://scipy.org/'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/scipy-sp/'),
    ('twitter', 'https://twitter.com/scipysp'),
    ('facebook', 'https://www.facebook.com/SciPySP/'),
)

DEFAULT_PAGINATION = 10
MENUITEMS = (('Arquivo', '/archives.html'),
	     ('Categorias', '/categories.html'),
	     ('Tags', '/tags.html'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/Flex"

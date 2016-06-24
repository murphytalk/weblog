#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import environ

AUTHOR = u'Mu Lu'
SITENAME = u"murphytalk's digitized memo"
#PUBLISH en var is set in Makefile publish goal
SITEURL = '' if environ.get('PUBLISH') is None else 'http://murphytalk.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'


PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["tag_cloud","tipue_search"]
THEME = "../pelican-themes/pelican-bootstrap3"

#pelican-bootstrap3
CUSTOM_CSS = 'static/custom.css'
BOOTSTRAP_FLUID = True

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'static/custom.css'}
}

USE_FOLDER_AS_CATEGORY = True
TYPOGRIFY = True

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

#URL
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

#Archive
YEAR_ARCHIVE_SAVE_AS  = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('The old blog', 'http://murphytalk-log.appspot.com/'),
#         ('The Portal', 'http://murphytalk.vicp.net/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

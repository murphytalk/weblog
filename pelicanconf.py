#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mu Lu'
SITENAME = u"murphytalk's digitized memo"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'


PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["tag_cloud"]
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

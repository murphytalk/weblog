#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import environ

CACHE_CONTENT = True

AUTHOR = u'Mu Lu'
SITENAME = u"murphytalk's digitized memo"
#PUBLISH en var is set in Makefile publish goal
SITEURL = '' if environ.get('PUBLISH') is None else 'http://murphytalk.github.io'
CC_LICENSE = 'CC-BY-NC'
PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%a %B %d %Y'


PLUGIN_PATHS = ["./plugin/pelican-plugins",'./plugin']

PLUGINS = [
    "tag_cloud",
    #http://duncanlock.net/blog/2013/05/29/better-figures-images-plugin-for-pelican/
    #"better_figures_and_images",
    "tipue_search",
    "pelican-ipynb.markup"
]
## Setting for the better_figures_and_images plugin
#RESPONSIVE_IMAGES = True
#FIGURE_NUMBERS = True


THEME = "./theme/pelican-bootstrap3"
#https://bootswatch.com/
#BOOTSTRAP_THEME = "readable"
DARK_THEME = False #will affect Twitter timeline

CUSTOM_CSS = 'static/custom.css'
BOOTSTRAP_FLUID = True

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'static/custom.css'}
}

DISPLAY_ARTICLE_INFO_ON_INDEX = True

USE_FOLDER_AS_CATEGORY = True
TYPOGRIFY = True
# SHARIFF = True  #social meida sharing
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

#URL
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

#Archive
ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS  = 'posts/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

#Sidebar
DISPLAY_TAGS_INLINE = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


LINKS = (
    ('<i class="fa fa-book fa-lg"></i>&nbsp;&nbsp;&nbsp;My Knowledge Base', 'http://murphytalk.pythonanywhere.com'),
    ('<i class="fa fa-pencil-square-o fa-lg"></i>&nbsp;&nbsp;&nbsp;My Private Diary', 'http://murphytalk.vicp.net/diary'),
    ('<i class="fa fa-anchor fa-lg"></i>&nbsp;&nbsp;&nbsp;My Online Portal', 'http://murphytalk.vicp.net'),
)

me = "murphytalk"
SOCIAL = True
MY_TWITTER_FEED = False
ABOUT_ME = None

RECENT_POST_COUNT = 25
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

#GITHUB_USER = me
TWITTER_CARDS = True
TWITTER_USERNAME = me
ADDTHIS_PROFILE = me
DEFAULT_PAGINATION = 10

#DISQUS_DISPLAY_COUNTS = True
#DISQUS_SITENAME = 'murphytalks-digit-memo'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

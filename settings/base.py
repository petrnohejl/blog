#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


# Blog name
SITENAME = u'Jestřáblog'
SITESUBTITLE = u'Život z ptačí perspektivy'
AUTHOR = u'Petr Nohejl'

# Pelican paths
PATH = '../content/'
OUTPUT_PATH = '../output/'
STATIC_PATHS = ('files', 'images', 'static/custom.css', 'CNAME', 'favicon.ico', 'robots.txt')
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
DELETE_OUTPUT_DIRECTORY = True
USE_FOLDER_AS_CATEGORY = False

# Language and time
TIMEZONE = 'Europe/Prague'
LOCALE = 'czech'
DEFAULT_LANG = u'cs'
DEFAULT_DATE_FORMAT = '%x'

# Blog settings
SUMMARY_MAX_LENGTH = 50
DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = u'Nezařazené'
WITH_FUTURE_DATES = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MD_EXTENSIONS = ('codehilite(css_class=highlight)', 'extra', 'headerid')

# URL and HTML file paths
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
YEAR_ARCHIVE_URL = 'archive/{date:%Y}/index'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
TAG_SAVE_AS = False
TAGS_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Feed
FEED_ATOM = 'feed.xml'
FEED_MAX_ITEMS = 10
FEED_ALL_ATOM  = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Theme
THEME = 'D:/GIT/FORKED/pelican-bootstrap3'
#THEME_STATIC_PATHS = ('static',)
#JINJA_FILTERS = filters
CUSTOM_CSS = 'static/custom.css'
PYGMENTS_STYLE = 'monokai'
SITELOGO = None
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
BOOTSTRAP_NAVBAR_INVERSE = False
FAVICON = 'favicon.ico'
HIDE_SIDEBAR = True
DISQUS_DISPLAY_COUNTS = False
CC_LICENSE = 'CC-BY-NC-SA'
CC_ATTR_MARKUP = False
USE_OPEN_GRAPH = True
BOOTSTRAP_THEME = 'cosmo'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False
ADDTHIS_FACEBOOK_LIKE = True
ADDTHIS_TWEET = True
ADDTHIS_GOOGLE_PLUSONE = True

# Services
GOOGLE_ANALYTICS = 'UA-17930136-2'
DISQUS_SITENAME = 'petrnohejl'
TWITTER_USERNAME = 'petrnohejl'
ADDTHIS_PROFILE = 'ra-530d2ad72de762c4'

# Blogroll
LINKS = (('Petr Nohejl', 'http://petrnohejl.cz/'),
        ('Blog Janie Milíčové', 'http://janie.jestrab.net/'),
        ('Javorové lístky', 'http://honzajavorek.cz/blog'),
        ('JarmArt', 'http://jarmart.cz/'),
        ('Terezčin BlogHýsek', 'http://terezka.8bit.cz/'),
        ('Pavčin blog', 'http://pavca.8bit.cz/'),
        ('Zuzejkova kultura', 'http://www.zuzikovakultura.blogspot.com/'),
        ('Bakinovy zážitky', 'http://www.bakinovyzazitky.blogspot.com/'),)

# Social widget
SOCIAL =   (('Twitter', 'http://twitter.com/petrnohejl'),
            ('LinkedIn', 'http://www.linkedin.com/in/petrnohejl'),
            ('GitHub', 'https://github.com/petrnohejl'),
            ('Facebook', 'http://www.facebook.com/petr.nohejl'),)

# Menu
MENUITEMS = (('Categories', '/categories.html'),
            ('Feed', '/feed.xml'),
            ('About me', 'http://petrnohejl.cz/'),)

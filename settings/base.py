#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
from datetime import date
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
DEFAULT_LANG = 'cs'
DEFAULT_DATE_FORMAT = '%x'

# Blog settings
SUMMARY_MAX_LENGTH = 50
DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = u'Blog'
WITH_FUTURE_DATES = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.headerid': {},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

# URL and HTML file paths
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
YEAR_ARCHIVE_URL = 'archive/{date:%Y}/index'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
ARCHIVES_SAVE_AS = 'archive.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAG_SAVE_AS = False
TAGS_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Feed
FEED_ALL_ATOM  = 'feed.xml'
FEED_MAX_ITEMS = 100
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = 'D:/GIT/GITHUB/MinimalXY'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2009
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Hi! I’m Petr – an Android developer living in Brno, Czech Republic.'
AUTHOR_DESCRIPTION = u'Hi! I’m Petr – an Android developer living in Brno, Czech Republic. I’m passionate about code, software architecture and technology. I studied at the Brno University of Technology and currently I work at STRV as team lead of the Android department. I’ve been developing mobile apps since 2009. I like #android #coffee #reggae #photography #djembe #traveling #valueinvesting #myfamily.'
AUTHOR_AVATAR = 'https://www.gravatar.com/avatar/8fafd9d1a430a1e843478f00c3da924a?s=240'
AUTHOR_WEB = 'https://petrnohejl.cz'

# Services
GOOGLE_ANALYTICS = 'UA-17930136-2'
DISQUS_SITENAME = 'petrnohejl'

# AddThis (not used)
ADDTHIS_PROFILE = 'ra-530d2ad72de762c4'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False
ADDTHIS_FACEBOOK_LIKE = True
ADDTHIS_TWEET = True

# Social
SOCIAL = (
    ('facebook', 'https://www.facebook.com/petr.nohejl'),
    ('instagram', 'https://www.instagram.com/petr.nohejl/'),
    ('twitter', 'https://twitter.com/petrnohejl'),
    ('github', 'https://github.com/petrnohejl'),
    ('linkedin', 'https://www.linkedin.com/in/petrnohejl'),
)

# Menu
MENUITEMS = (
    ('Categories', '/' + CATEGORIES_SAVE_AS),
    ('Archive', '/' + ARCHIVES_SAVE_AS),
)

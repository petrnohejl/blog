#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from base import *


# Site URL
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = True

# URL and HTML file paths
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
YEAR_ARCHIVE_URL = 'archive/{date:%Y}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'

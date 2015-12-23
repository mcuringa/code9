#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'mxc'
SITENAME = 'Code Club 9'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['img', 'res', 'css', 'js']

THEME = "/home/mxc/Documents/code9/themes/code9"


PLUGIN_PATHS = ['/home/mxc/Documents/pelican-plugins']
PLUGINS = ['pandoc_reader']

PANDOC_ARGS = [
  '--mathjax',
  '--smart',
  '--toc',
  '--toc-depth=2',
]

# PANDOC_EXTENSIONS = [
#   '+hard_line_breaks',
#   '-citations'
# ]

PAGE_ORDER_BY = 'weight'

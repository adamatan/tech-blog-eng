#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Matan'
SITENAME = u'Adam Matan'
# SITEURL = 'https://adammatan.com'
SITESUBTITLE = ''
THEME = 'gum'
DISQUS_SITENAME = "atb"

PATH = 'content'

STATIC_PATHS = ['images']
GOOGLE_ANALYTICS_ID = 'UA-74046927-1'
TWITTER_USERNAME = 'adam_matan'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
            ('Stackoverflow', 'stackoverflow.com/users/51197/adam-matan'),
            ('github',        'https://github.com/adamatan'),
            ('@adam_matan',   'https://twitter.com/adam_matan'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

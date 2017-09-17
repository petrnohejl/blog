#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import re
import sys
import unicodedata
import datetime
from fabric.api import *


# paths
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
CONTENT_PATH = PROJECT_PATH + '/content'
OUTPUT_PATH = PROJECT_PATH + '/output'


def clean():
	"""Clean output"""
	if os.path.isdir(DEPLOY_PATH):
		local('rm -rf {deploy_path}'.format(**env))
		local('mkdir {deploy_path}'.format(**env))


def build():
	"""Build website with development settings"""
	local('pelican -s settings/development.py')


def rebuild():
	"""Clean and build"""
	clean()
	build()


def regenerate():
	"""Autoreloading building of website with development settings"""
	local('pelican -r -s settings/development.py')


def serve():
	"""Run server"""
	fastprint('Serving website on http://localhost:8000/', end='\n')
	local('cd {deploy_path} && python -m SimpleHTTPServer 8000'.format(**env))


def reserve():
	"""Build and run server"""
	build()
	serve()


def build_production():
	"""Build website with production settings"""
	local('pelican -s settings/production.py')


def commit_master():
	"""Commit web sources to Git repo"""

	with lcd(PROJECT_PATH):
		local('git add -A .')
		with settings(hide('warnings'), warn_only=True):
			local('git commit -m "Publish"')
		#local('git push origin master')

	fastprint('\n\nIgnored files:', end='\n')
	local('git clean -ndX')


def commit_ghp():
	"""Build and deploy website to GitHub Pages"""

	# build
	with lcd(PROJECT_PATH):
		#local('touch content') # prevent caching
		build_production()

	# deploy
	with lcd(OUTPUT_PATH):
		#unnecessary = ['author']
		#local('rm -rf ' + ' '.join(unnecessary))
		#local('python {0}/Scripts/ghp-import -m Deploy -p {1}'.format(sys.prefix, OUTPUT_PATH))
		local('python {0}/Scripts/ghp-import -m Deploy {1}'.format(sys.prefix, OUTPUT_PATH))


def publish():
	"""Push web sources, build and deploy website"""
	commit_master()
	commit_ghp()
	fastprint(u"Don't forget to push both branches!", end='\n')


def new(title=None):
	"""Create new article template"""

	if not title:
		fastprint('>>> Enter title: ')
		title = prompt('')
		title = title.decode('cp852')
	else:
		title = title.decode('cp1250')

	slug = __slugify(title)
	date = datetime.datetime.now() + datetime.timedelta(hours=2)
	filename = '{0}_{1}.md'.format(date.strftime('%Y-%m-%d'), slug)
	path = os.path.join(CONTENT_PATH, filename)
	content = u'Title: {0}\nCategory: {1}\n\n'.format(title, u'Nezařazené')

	with open(path, 'w') as f:
		f.write(content.encode('utf8'))

	fastprint(u'Successfully created new article "{0}" in "{1}"'.format(title, path), end='\n')


def __slugify(string, underscore=False):
	if not isinstance(string, unicode):
		string = unicode(string)
	string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore')
	string = unicode(re.sub(r'[^\w\s-]', '', string).strip().lower())

	re_dash = re.compile(r'[-_\s]+' if underscore else r'[-\s]+')
	return re_dash.sub('-', string)

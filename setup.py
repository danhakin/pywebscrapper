try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A simple web scrapper in python',
	'author': 'danhakin',
	'url' : 'git@github.com:danhakin/pywebscrapper.git',
	'download_url' : 'https://github.com/danhakin/pywebscrapper.git',
	'author_email' : 'danhakin@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['pywebscrapper'],
	'scripts' : [],
	'name' : 'pywebscrapper'
}

setup(**config)	
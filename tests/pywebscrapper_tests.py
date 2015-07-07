from nose.tools import *
import pywebscrapper.webscrapper as ws

def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"

def test_hello():
	assert ws.hello() == 'hello'
#!/usr/bin/python
# -*- coding: utf8 -*-

import urllib2
import re

alphabet = u"ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ"

def readPage(letter):
	url = u"http://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(" + letter + ")"
	header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-9,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	
	req = urllib2.Request(url.encode('utf-8'), headers = header)
	try:
	    page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
	    print e.fp.read()
	content = page.read()
	words = re.findall('<li><a[^>]*>([^<]+)<\/a>', content, flags=0)
	words.pop()
	print "Read the letter ", letter
	return words

def getWordList():
	words = []
	for letter in alphabet:
		words += readPage(letter)
	return words

def writeToFile(filename):
	f = open(filename, 'w')
	f.write("\n".join(getWordList()))
	f.close()

writeToFile("words.txt")
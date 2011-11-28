#!/usr/bin/python
# coding: utf-8

import urllib, sys, os, cache_mgr, platform
from xml.dom.minidom import parseString 
from color import lgreen, dgreen, lwhite, lgreen_s, ed

def get_clip():
	pf = platform.system().upper()
	if pf.startswith('CYGWIN'):
		with open('/dev/clipboard') as clipboard:
			clip = clipboard.read()
	# 没人在Windows下用这个吧？
	#elif pf.startswith('WINDOWS'):
		#import win32clipboard
		#win32clipboard.OpenClipboard()
		#clip = win32clipboard.GetClipboardData()
		#win32clipboard.CloseClipboard()
	elif pf.startswith('LINUX'):
		clip = os.popen('xsel').read()
	return clip

def get_node_text(nodelist):
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			return node.data 

def get_tag_text(xml, tagName, addin=''):
	if len(xml.getElementsByTagName(tagName)) > 0:
		return get_node_text(xml.getElementsByTagName(tagName)[0].childNodes) + addin

def found_nothing(xml):
	if xml.getElementsByTagName('sugg'):
		print_sugg(xml)
		return True
	elif get_tag_text(xml, 'def') == 'Not Found':
		print lgreen('Sorry, no result.')
		return True
	else:
		return False

def print_sugg(xml):
	suggs = xml.getElementsByTagName('sugg')
	print lgreen('Are you looking for the following:')
	for sugg in suggs:
		print get_node_text(sugg.childNodes)

def print_result(xml):
	pron = get_tag_text(xml, 'pron')
	if not pron:
		pron = u'No soundmark'
	print "\n %s [%s]\n" % (lgreen(get_tag_text(xml, 'key')), dgreen(pron))
	print lwhite(get_tag_text(xml, 'def', '\n'))
	sents = xml.getElementsByTagName('sent')
	for sent in sents:
		print " %s" % get_tag_text(sent, 'orig').replace('<em>', lgreen_s).replace('</em>', ed)
		print " %s\n" % dgreen(get_tag_text(sent, 'trans'))
	print '\n'

if __name__ == "__main__":
	api_url = u"http://dict.cn/ws.php?utf8=true&q="
	try:
		word = sys.argv[1]
		if not isinstance(word, unicode):
			word = word.decode('utf-8')
	except IndexError:
		word = get_clip().decode('utf-8')
	cache = cache_mgr.cache_mgr()
	xml_str = cache.is_word_exist(word)
	if not xml_str:
		try:
			xml_str = urllib.urlopen(api_url + urllib.quote(word.encode('utf-8'))).read()
		except IOError:
			print u'Please Check the network.'
			exit()
		if not isinstance(xml_str, unicode):
			xml_str = xml_str.decode('utf-8')
	xml = parseString(xml_str.encode('utf-8'))
	if not found_nothing(xml):
		print_result(xml)
		cache.cache_word(word, xml_str)

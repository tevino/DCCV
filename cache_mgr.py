# coding: utf-8

import sqlite3, shutil, os, sys

currentdir = sys.path[0]
cache = currentdir + '/cache.db'
if not os.path.isfile(cache):
	orig = cache + '.empty'
	if os.path.isfile(orig):
		shutil.copyfile(orig, cache)    
	else:
		print u'empty cache file does not exist\n please copy a new one(%s) to %s' % (orig, os.getcwd())
		exit()

class cache_mgr:
	def __init__(self):
		self.con = sqlite3.connect(cache)
		self.db = self.con.cursor()

	def is_word_exist(self, word):
		assert isinstance(word,unicode)
		self.db.execute('SELECT COUNT(*) FROM words WHERE word=?', (word,))
		count = self.db.fetchone()
		if count > 0:
			return self.get_exp(word) 
		else:
			return False

	def get_exp(self, word):
		assert isinstance(word,unicode)
		self.db.execute('SELECT exp FROM words WHERE word=?', (word,))
		exp = self.db.fetchone()
		if exp:
			exp = exp[0]
		return exp

	def cache_word(self, word, exp):
		assert isinstance(word,unicode)
		assert isinstance(exp,unicode)
		if self.is_word_exist(word):
			return False
		else:
			self.db.execute('INSERT INTO words VALUES(?,?)', (word, exp,))
			self.db.fetchone()

	def __del__(self):
		self.db.close()
		self.con.commit()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import shelve
import os.path

currentdir = sys.path[0]
cache_file = os.path.join(currentdir, '.cache.db')


class CacheMgr:
    def __init__(self):
        self.db = shelve.open(cache_file, 'c')

    def _is_word_exist(self, word):
        assert isinstance(word, str)
        return word in self.db

    def get_exp(self, word):
        assert isinstance(word, str)
        if self._is_word_exist(word):
            return self.db[word]
        else:
            return None

    def cache_word(self, word, exp):
        assert isinstance(word, str)
        assert isinstance(exp, str)
        if self._is_word_exist(word):
            return False
        else:
            self.db[word] = exp

    def __del__(self):
        self.db.close()

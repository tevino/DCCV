#!/usr/bin/python
# coding: utf-8

ed = u'\033[0m'

lgreen_s = u'\033[1;32m'
dgreen_s = u'\033[0;32m'
lwhite_s = u'\033[1m'


def rig(st, s):
    return u'%s%s%s' % (st, s, ed)


def lgreen(s):
    return rig(lgreen_s, s)


def dgreen(s):
    return rig(dgreen_s, s)


def lwhite(s):
    return rig(lwhite_s, s)

if __name__ == '__main__':
    print u'normal'
    print lgreen(u'light green')
    print dgreen(u'dark green')
    print lwhite(u'white')

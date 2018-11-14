#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''

class Base(object):

    def __new__(cls, *args, **kwargs):
        print('base')
        return cls(*args, **kwargs)

    def __init__(self):
        print('base init')


class Common(Base):
    def __init__(self):
        print('common')


Common()
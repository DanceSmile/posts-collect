#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''

import  functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kw):
            print(text)
            return func(*args, **kw)
        return wrap
    return decorator
@log('start logging')
def now():
    print('2015-3-25')

now()

print(__file__)

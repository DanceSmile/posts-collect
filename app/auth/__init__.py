#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''

from flask  import  Blueprint


auth =  Blueprint('auth', __name__)

from . import  views

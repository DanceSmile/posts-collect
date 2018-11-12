#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
from . import  auth
from flask import  render_template


@auth.route('/login')
def login():
    return  render_template('auth/login.html')


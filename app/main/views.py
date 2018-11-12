#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''

from flask  import  render_template, redirect, session, url_for


from . import  main


@main.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')


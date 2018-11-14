#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''

from flask  import  render_template, redirect, session, url_for
from flask_login import login_required

from . import  main


@main.route('/', methods=['GET', "POST"])
def index():
    print(session['user_id'])
    return render_template('index.html')


@main.route('/secret')
@login_required
def secret():
    return 'only authenticated users are allowed'

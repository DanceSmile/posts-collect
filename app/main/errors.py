#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
from . import  main
from flask import  render_template

@main.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'),404

@main.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'),500
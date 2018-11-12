#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
from flask import Blueprint

main = Blueprint('main', __name__)


from . import  views, errors



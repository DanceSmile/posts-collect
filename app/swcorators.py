#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
from functools import wraps
from flask import Flask, abort
from flask_login import  current_user
from models import  Permission
def permission_required(permission):
    def decorator(fun):
        @wraps(fun)
        def decorated(*args, **kw):
            if not current_user.can(permission):
                abort(403)
            return fun(*args, **kw)
        return decorated
    return decorator

def admin_required(fun):
    return permission_required(Permission.admin)(fun)
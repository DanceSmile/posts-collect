#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
from . import  auth
from flask import  render_template, redirect, flash
from .forms import   LoginForm
from flask_login import  current_user
from  ..models import User
from flask_login import login_user





@auth.route('/login', methods=['GET', "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is  not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            redirect('main.index')
        flash('Invalid username or password')
    return  render_template('auth/login.html', form=form,current_user=current_user)



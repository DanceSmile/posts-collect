#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
import email

from . import  auth
from flask import render_template, redirect, flash, request, url_for
from .forms import  LoginForm, RegisterForm
from flask_login import  current_user, login_required, logout_user,login_user
from  ..models import User
from  .. import  db




@auth.route('/login', methods=['GET', "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is  not None and user.verify_password(form.password.data):
            print(user)
            login_user(user, form.remember_me.data)
            return  redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return  render_template('auth/login.html', form=form,current_user=current_user)


@auth.route('/logout', methods=['GET', "POST"])
def login_out():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form  = RegisterForm()

    if form.validate_on_submit():
        user = User(username = form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        flash('you can login ')
        return  redirect(url_for('main.index'))
    return render_template('auth/register.html',form=form)


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()



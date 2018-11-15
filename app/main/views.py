#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''

from flask  import  render_template, redirect, session, url_for, abort
from flask_login import login_required, current_user
from app.models import  User
from . import  main
from .forms import EditProfileForm
from app import  db
@main.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')


@main.route('/secret')
@login_required
def secret():
    return 'only authenticated users are allowed'


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)

@main.route('/edit-profile',methods=['GET',"POST"])
@login_required
def edit_profile():
    form  = EditProfileForm()
    print(current_user.about_me)
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        return redirect(url_for('main.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return  render_template('useredit.html',form=form)
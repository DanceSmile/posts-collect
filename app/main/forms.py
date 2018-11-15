#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo

class EditProfileForm(Form):
    name = StringField('real name', validators=[Length(0,64)])
    location = StringField("location", validators=[Length(0,64)])
    about_me = TextAreaField('about me', validators=[Length(0,64)])
    submit = SubmitField('edit')

class
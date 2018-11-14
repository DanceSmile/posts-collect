#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from app.models import User


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegisterForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('username', validators=[Required(),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, numbers, dots or underscores')
                                                   ])
    password = StringField('password',
                           validators=[Required(), Length(6, 64), EqualTo('password2', 'password musr match')])
    password2 = StringField('password2', validators=[Required(), Length(6, 64)])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email is already registered')


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username is already in use')

#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''

from . import  db
from werkzeug.security import generate_password_hash, check_password_hash
from . import  login_manager
from flask_login import  UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(UserMixin, db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship("User", backref='role')

    @staticmethod
    def insert_roles():

        roles = {
            'User' : (Permissions.FOLLOW | Permissions.COMMENT | Permissions.WRITE_ARTICLE, True),
            'Moderator': (Permissions.FOLLOW | Permissions.COMMENT | Permissions.WRITE_ARTICLE | Permissions.MODERATE_COMMENTS, True)
            "Administrator": (0xff, False)
        }

        for role in roles:
            Role.query.filter_by()


    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise  AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<Role %r>' % self.username

class Permissions:
    FOLLOW=0x01
    COMMENT=0x02
    WRITE_ARTICLE=0x04
    MODERATE_COMMENTS=0x08
    ADMINISTER=0x80
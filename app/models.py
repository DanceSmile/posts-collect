#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''

from . import  db
from werkzeug.security import generate_password_hash, check_password_hash
from . import  login_manager
from flask_login import  UserMixin, AnonymousUserMixin
from datetime import  datetime


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
            'Moderator': (Permissions.FOLLOW | Permissions.COMMENT | Permissions.WRITE_ARTICLE | Permissions.MODERATE_COMMENTS, False),
            "Administrator": (0xff, False)
        }

        for role in roles:
            r  = Role.query.filter_by(name=role).first()
            if r is  None:
                r = Role(name = role)
            r.permissions = roles[role][0]
            r.default = roles[role][1]
            db.session.add(r)
        db.session.commit()





    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.Text())
    location = db.Column(db.String(64))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen  = db.Column(db.DateTime(), default=datetime.utcnow)
    def  can(self, permissions):
        return self.role is not None and ( self.role.permissions & permissions) == permissions

    def id_admin(self):
        return self.can(Permissions.ADMINISTER)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)


    def __init__(self, **kw):
        super(User, self).__init__(**kw)
        if self.role is None:
            if self.email == '1215850394@qq.com' :
                self.role = Role.query.filter_by(permissions=0xff).first()
            else:
                self.role = Role.query.filter_by(default=True).first()
    @property
    def password(self):
        raise  AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User %r>' % self.username

class AnonymousUser(AnonymousUserMixin):
     def can(self, permissions):
         return False
     def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


class Permissions:
    FOLLOW=0x01
    COMMENT=0x02
    WRITE_ARTICLE=0x04
    MODERATE_COMMENTS=0x08
    ADMINISTER=0x80
#!/usr/bin/env python3
# encoding: utf8
'''
@author zero
'''
import os
from app import  create_app, db
from flask_script import Manager, Shell
from flask_migrate import  Migrate, MigrateCommand
from app.models import  User, Role

def make_shell_context():
    return dict(db=db, app=app, User=User, Role=Role)

app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
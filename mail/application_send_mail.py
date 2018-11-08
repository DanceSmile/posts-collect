#!/usr/bin/env python3
# encoding: utf8

'''
@author zero
为了避免每次都手动编写电子邮件消息
我们最好把程序发送电子邮件的通用部分抽象出来
'''
from flask import  Flask, render_template
from flask_mail import Mail, Message
from threading import  Thread
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# send mail
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_SUBJECT_PREFIX'] = '[Flask]'
app.config['FLASKY_MAIL_SENDER'] = 'flask Admin <1215850394@qq.com>'


mail = Mail(app)

def send_mail(to, subject, template, **kw):
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] +  ' ' +  subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.html = render_template(template, **kw)
    mail.send(msg)

def thread_send(app, name):
    with app.app_context():
        send_mail('1215850394@qq.com', 'hello flask user  %s' % name, 'mail.html', name=name)

@app.route('/<name>')
def index(name):
    thr = Thread(target=thread_send, args=(app, name))
    thr.start()
    return render_template('mail.html', name=name)
if __name__ == "__main__":
    app.run(debug=True)











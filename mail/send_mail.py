'''
send mail  by flask-mail
'''
from flask import  Flask
from flask_script import Manager
from flask_mail import  Mail, Message
import os

app = Flask(__name__)

'''
MAIL_SERVER localhost 电子邮件服务器的主机名或 IP 地址
MAIL_PORT 25 电子邮件服务器的端口
MAIL_USE_TLS False 启用传输层安全(Transport Layer Security,TLS)协议
MAIL_USE_SSL False 启用安全套接层(Secure Sockets Layer,SSL)协议
MAIL_USERNAME None 邮件账户的用户名
MAIL_PASSWORD None 邮件账户的密码
'''
app.config["MAIL_SERVER"] = 'smtp.qq.com'
app.config['MAIL_USE_TLS'] = True
app.config["MAIL_PORT"] = 25

app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

manager = Manager(app)
mail = Mail(app)


msg = Message('test flask mail', sender='1215850394@qq.com', recipients=['1215850394@qq.com'])
msg.body = 'body mail'

print(app)

if __name__ == '__main__':
    with app.app_context():
        mail.send(msg)

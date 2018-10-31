# coding:utf-8
'''
程序的基本结构
'''

# 编写并运行第一个 Flask Web 程序

# wsgi服务器将客户端请求装转交给app对象处理

from flask import Flask
from flask import request
from flask import make_response
from flask_script  import  Manager

# 初始化程序实例
'''
__name__
Flask 用这个参数决定程序的根目录，
以便稍后能够找到相对于程序根目录的资源文件位置
'''
app = Flask(__name__)


# 路由和视图模版
@app.route('/')
def index():
    # Flask 使用上下文临时把 request 对象 变为全局可访问 

    '''
    注意在这个视图函数中我们如何把 request 当作全局变量使用。
    事实上，request 不可能是 全局变量。
    试想，在多线程服务器中，多个线程同时处理不同客户端发送的不同请求时，
    每个线程看到的 request 对象必然不同。
    Falsk 使用上下文让特定的变量在一个线程中全局 可访问，
    与此同时却不会干扰其他线程。
    '''
    user_agent = request.headers.get('User-Agent')
    return '<h1> hello flask ...</h1><p> user-agent is %s' % user_agent    


@app.route('/user/<name>')
def user(name):
    return '<h1>hello %s</h1>' % name


# 路由函数重载
@app.route('/user/<int:id>')
def user_id(id):
    return 'user_id is %s' % id


@app.route('/user/<float:height>')
def get_user_height(height):
    return 'the param float is %s' % height

# @app.route('/test/<path:path>')
# def get_path(path):
#     return path



@app.route('/make_response')
def make_response_call():
    status  = 200
    header = {'name': 'zero'}
    response = make_response('<p> make response with cookie username = zero</p>', status, header)
    response.set_cookie('username', 'zero')

    return response
    


@app.route('/bad')
def bad_request():
    status =  400
    header = {'name': 'zero'}
    return "bad request", status, header
#请求调度
'''
pip
使用app.url_map来查看url与视图函数的映射关系
'''

# flask extsion shell command
manager = Manager(app)

print(app.url_map)
if __name__  == '__main__' :
    # 启动程序
    manager.run()
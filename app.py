from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name
@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))
    print(url_for('user_page', name='dfsfs'))
    print(url_for('user_page', name=24234, flask=434, amd=3423))

    return 'Test page'

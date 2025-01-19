from flask import Flask

# 创建 Flask 应用实例
app = Flask(__name__)

# # 定义一个路由，响应首页请求
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return 'This is the about page.'
# 运行应用
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('index.html', name='Flask User')

if __name__ == '__main__':
    app.run(debug=True)
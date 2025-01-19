from flask import Flask

app = Flask(__name__)

#注册路由
@app.route('/')
# route()第一个参数就是URL规则，字符串表示
def index():
    return '<h1>Hello World</h1>'
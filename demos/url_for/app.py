from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"
@app.route('/login')
def login():
    return "请登录！"

if __name__ == '__main__':
    app.run(debug=True)
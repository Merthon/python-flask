from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/test')
def test():
    return f'URL for home page is {url_for("home")}'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

# 创建flask应用实例
app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username'] 
        return f"Hello, {username}!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

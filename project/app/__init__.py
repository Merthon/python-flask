from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # 使用 SQLite 数据库

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .auth_routes import auth
    app.register_blueprint(auth)

    return app

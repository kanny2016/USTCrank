from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(use_native_unicode='utf-8')
bootstrap =  Bootstrap()

def create_app():
    app = Flask(__name__)
    # 数据库地址
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ubuntu/USTCrank/scores.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    # 表单 防CSRF
    app.config['SECRET_KEY'] = 'USTC'
    # 排名每页显示人数
    app.config['USERS_PER_PAGE'] = 100

    db.init_app(app)
    bootstrap.init_app(app)

    from .main import main_view
    app.register_blueprint(main_view)

    return app


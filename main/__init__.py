from flask import Flask
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy

# 导入配置
from config import Config

# 鉴权实例
auth = HTTPTokenAuth(scheme = 'JWT')

# 数据库实例
db = SQLAlchemy()

# 工厂函数
def create_app():
    # 应用实例
    app = Flask(__name__)
    app.config.from_object(Config)

    # 数据库初始化
    db.init_app(app)

    # 注册蓝本
    from main.api import api
    app.register_blueprint(api, url_prefix = '/api')

    return app

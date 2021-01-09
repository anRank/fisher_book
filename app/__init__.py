from flask import Flask
from flask_login import LoginManager
from app.models.book import db
from flask_mail import Mail
from flask_cache import Cache
from app.libs.limiter import Limiter

# flask-login提供flask的用户会话管理。处理登录，注销和记住会话的常见任务 https://flask-login.readthedocs.io/en/latest/#installation
# 创建LoginManager类
login_manager = LoginManager()
mail = Mail()
# cache = Cache(config={'CACHE_TYPE': 'simple'})
limiter = Limiter()


def create_app():
    app = Flask(__name__)
    # 注入配置信息
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    # 配置login_manager.init_app(app) 进行登录
    login_manager.init_app(app)
    # 登录视图的名称可以设置为LoginManager.login_view
    login_manager.login_view = 'web.login'
    # 闪烁的默认消息是“要自定义消息”
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)

    # 创建所有数据表
    with app.app_context():
        db.create_all()
    return app


# 注册蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
# 这里不另外定义函数，直接在create_app()中注册也是一样的

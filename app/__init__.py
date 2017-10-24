# -*- encoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
app.secret_key = 'nowcoder'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
# 用来控制登陆页面
login_manager.login_view = '/register-login/'
# 用来控制fresh login页面
login_manager.refresh_view = "/re-login/"


from app import views, models

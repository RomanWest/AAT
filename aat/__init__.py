import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.debug import DebuggedApplication


app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2058816:Kejinmysql2021@csmysql.cs.cf.ac.uk:3306/c2058816_aat'
app.config['SECRET_KEY'] = 'd530f8e038ee2524ec69e2f37bceeb44eb14473aa2853aeb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from aat import routes
from flask_admin import Admin
from aat.views import AdminView
from flask_admin.contrib.sqla import ModelView
from aat.models import User

admin = Admin(app,name='Admin panel',template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

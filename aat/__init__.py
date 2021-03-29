import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#import sqlite3

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'd530f8e038ee2524ec69e2f37bceeb44eb14473aa2853aeb'
app.config['SQLALCHEMY_DATABASE_URI'] = #link to sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from aat import routes 

from flask_admin import Admin
from aat.views import AdminView
from aat.models import User
admin = Admin(app,name='Admin panel',template_mode='bootstrap3')
admin.add_view(AdminView(User, db.session))

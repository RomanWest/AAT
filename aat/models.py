from datetime import datetime
from aat import db, login_manager
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Attempts(db.Model):
	attempt_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, nullable=False)
	assessment_id = db.Column(db.Integer, nullable=False)
	attempt_no = db.Column(db.Integer, nullable=False)
	answer_1 = db.Column(db.String, nullable=False)
	correct_1 = db.Column(db.Boolean, nullable=False)
	answer_2 = db.Column(db.String, nullable=False)
	correct_2 = db.Column(db.Boolean, nullable=False)
	answer_3 = db.Column(db.String, nullable=False)
	correct_3 = db.Column(db.Boolean, nullable=False)
	percentage_correct = db.Column(db.Float, nullable=False)
	module_code = db.Column(db.String,nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	is_formative = db.Column(db.Boolean,nullable=False)

class Multiple(db.Model):
	quesion_id = db.Column(db.Integer,primary_key=True)
	question = db.Column(db.String, nullable=False)
	correct = db.Column(db.String, nullable=False)
	module_code = db.Column(db.String,nullable=False)
	incorrect_1 = db.Column(db.String,nullable=False)
	incorrect_2 = db.Column(db.String,nullable=False)
	incorrect_3 = db.Column(db.String,nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	difficulty = db.Column(db.String, nullable=False)
	is_formative = db.Column(db.Boolean,nullable=False)
	feedback = db.Column(db.String,nullable=False)
	
class Fill(db.Model):
	quesion_id = db.Column(db.Integer,primary_key=True)
	question = db.Column(db.String, nullable=False)
	module_code = db.Column(db.String,nullable=False)
	correct = db.Column(db.String, nullable=False)
	blank_1 = db.Column(db.String,nullable=False)
	blank_2 = db.Column(db.String,nullable=False)
	blank_3 = db.Column(db.String,nullable=False)
	difficulty = db.Column(db.String, nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	is_formative = db.Column(db.Boolean,nullable=False)
	feedback = db.Column(db.String,nullable=False)

class Assessment(db.Model):
	assessment_id = db.Column(db.Integer,primary_key=True)
	assessment_name = db.Column(db.String, nullable=False)
	module_code = db.Column(db.Integer,nullable=False)
	admin_created = db.Column(db.Boolean,nullable=False)
	q1_type = db.Column(db.String, nullable=False)
	q1_id = db.Column(db.String, nullable=False)
	q2_type = db.Column(db.String, nullable=False)
	q2_id = db.Column(db.String, nullable=False)
	q3_type = db.Column(db.String, nullable=False)
	q3_id = db.Column(db.String, nullable=False)


	def __repr__(self):
		return f"Assessment('{self.username}','{self.email}')"

class User(db.Model, UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(15),unique=True,nullable=False)
	first_name=db.Column(db.String(20),unique=True,nullable=False)
	last_name=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	password_hash=db.Column(db.String(128))
	password=db.Column(db.String(60),nullable=False)
	is_admin = db.Column(db.Boolean, nullable=False,default=False)
	module_1 = db.Column(db.String(20), nullable=False)
	module_2 = db.Column(db.String(20), nullable=False)
	module_3 = db.Column(db.String(20), nullable=False)


	
	def __repr__(self):
		return f"User('{self.username}','{self.email}')"


@property
def password(self):
		raise AttributeError('password is not a readable attribute')

@password.setter
def password(self,password):
	self.password_hash=generate_password_hash(password)

def verify_password(self,password):
	return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
from datetime import datetime
from aat import db, login_manager
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#Attempts class contains student attempt records
class Attempts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	#who has attempted
	user_id = db.Column(db.Integer)
	#which assessment attempted
	assessment_id = db.Column(db.Integer)
	assessment_name = db.Column(db.String(150), nullable=False)
	attempt_no = db.Column(db.Integer, nullable=False)
	answer_1 = db.Column(db.String(200), nullable=False)
	correct_1 = db.Column(db.Boolean, nullable=False)
	feedback_1 = db.Column(db.String(200), nullable=False)
	answer_2 = db.Column(db.String(200), nullable=False)
	correct_2 = db.Column(db.Boolean, nullable=False)
	feedback_2 = db.Column(db.String(200), nullable=False)
	answer_3 = db.Column(db.String(200), nullable=False)
	correct_3 = db.Column(db.Boolean, nullable=False)
	feedback_3 = db.Column(db.String(200), nullable=False)
	percentage_correct = db.Column(db.Float, nullable=False)
	module_code = db.Column(db.String(200),nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	is_summative = db.Column(db.Boolean,nullable=False)

#multiple means multiple choice type question
class Multiple(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	question = db.Column(db.String(200), nullable=False)
	correct = db.Column(db.String(200), nullable=False)
	module_code = db.Column(db.String(200),nullable=False)
	incorrect_1 = db.Column(db.String(200),nullable=False)
	incorrect_2 = db.Column(db.String(200),nullable=False)
	incorrect_3 = db.Column(db.String(200),nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	difficulty = db.Column(db.String(200), nullable=False)
	is_summative = db.Column(db.Boolean,nullable=False)
	feedback = db.Column(db.String(200),nullable=False)

	def __repr__(self):
    		return f"Multiple('{self.id}', '{self.question}', '{self.is_summative}')"

#fill means fill in the blanks type question
class Fill(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	question = db.Column(db.String(200), nullable=False)
	module_code = db.Column(db.String(200),nullable=False)
	correct = db.Column(db.String(200), nullable=False)
	difficulty = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	is_summative = db.Column(db.Boolean,nullable=False)
	feedback = db.Column(db.String(200),nullable=False)
		

multiple_q = db.Table(
    "multiple_q",
    db.Column("multiple_id", db.Integer, db.ForeignKey("multiple.id")),
    db.Column("assessment_id", db.Integer, db.ForeignKey("assessment.id")),
)

fill_q = db.Table(
    "fill_q",
    db.Column("fill_id", db.Integer, db.ForeignKey("fill.id")),
    db.Column("assessment_id", db.Integer, db.ForeignKey("assessment.id")),
)

#Assessment is a collection of 3 questions that could be fill or multiple
class Assessment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	#lecturer that made it
	user_id = db.Column(db.Integer)
	is_summative = db.Column(db.Boolean,nullable=False)
	assessment_name = db.Column(db.String(200), nullable=False)
	module_code = db.Column(db.String(200),nullable=False)
	admin_created = db.Column(db.Boolean,nullable=False)
	q1_type = db.Column(db.String(200), nullable=False)
	q1_id = db.Column(db.Integer, nullable=False)
	q1_feedback = db.Column(db.String(200), nullable=False)
	q2_type = db.Column(db.String(200), nullable=False)
	q2_id = db.Column(db.Integer, nullable=False)
	q2_feedback = db.Column(db.String(200), nullable=False)
	q3_type = db.Column(db.String(200), nullable=False)
	q3_id = db.Column(db.Integer, nullable=False)
	q3_feedback = db.Column(db.String(200), nullable=False)
	multiple_q = db.relationship("Multiple", secondary=multiple_q, primaryjoin=(multiple_q.c.assessment_id==id), 
				backref=db.backref("multiple_q"), lazy="dynamic")
	fill_q = db.relationship("Fill", secondary=fill_q, primaryjoin=(fill_q.c.assessment_id==id),
				backref=db.backref("fill_q"), lazy="dynamic")
	feedback_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"Assessment('{self.assessment_name}')"


#the users, both admin and students
class User(db.Model, UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(15),unique=True,nullable=False)
	first_name=db.Column(db.String(20),unique=True,nullable=False)
	last_name=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	password_hash=db.Column(db.String(128))
	password=db.Column(db.String(60),nullable=False)
	is_admin = db.Column(db.Boolean,default=False)
	module_1 = db.Column(db.String(20), nullable=True)
	module_2 = db.Column(db.String(20), nullable=True)
	module_3 = db.Column(db.String(20), nullable=True)

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

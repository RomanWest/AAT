from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError, Regexp
from flask_babel import _, lazy_gettext as _l
from aat.models import User
from flask import request
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=1,max=15)])
    first_name = StringField('First Name',validators=[DataRequired(),Length(min=1,max=20)])
    last_name = StringField('Last Name',validators=[DataRequired(),Length(min=1,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(message="Please enter a valid email address.")])
    password = PasswordField('Password',validators=[DataRequired(), Regexp('^.{6,8}$', message="Your password should be between 6 and 8 characters long.")])
    confirm_password = PasswordField(validators=[DataRequired(),EqualTo('password', message = "Your passwords dont match.")])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already exists. Please choose a different one.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email address is already associated with an account.")

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class FillQForm(FlaskForm):
    question = StringField('question', validators=[DataRequired()])
    module = StringField('module', validators=[DataRequired()])
    answer = StringField('answer', validators=[DataRequired()])
    incorrectfeedback = StringField('incorrectfeedback',validators = [DataRequired()])
    issummative = BooleanField('issummative', default = False, validators=[DataRequired()])
    difficulty = SelectField('difficulty', choices=[('easy','Easy'), ('hard', 'Hard')], validators=[DataRequired()])
    save = SubmitField('Save Question')


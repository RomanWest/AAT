from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired
from aat.models import Multiple

class MCForm(FlaskForm):
    question = StringField('question', validators=[DataRequired(), Length(min=3)])
    correct = StringField('correct', validators=[DataRequired()])
    module_code = StringField('module_code', validators=[DataRequired()])
    incorrect_1 = StringField('incorrect_1', validators=[DataRequired()])
    incorrect_2 = StringField('incorrect_2', validators=[DataRequired()])
    incorrect_3 = StringField('incorrect_3', validators=[DataRequired()])
    difficulty = SelectField('difficulty', choices=[('easy','easy'),('medium','medium'),('hard','hard')], validators=[DataRequired()])
    is_formative = BooleanField('is_formative')
    feedback = StringField('feedback', validators=[DataRequired()])
    submit = SubmitField('Upload')

    def validate_question(self, question):
        quest = Multiple.query.filter_by(question=question.data).first()
        if quest is not None:
            raise ValidationError('This Question is already in the database')

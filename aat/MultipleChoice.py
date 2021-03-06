from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired
from aat.models import Multiple, Assessment
from aat import app, db
from sqlalchemy import desc

class MCForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired(), Length(min=3)])
    correct = StringField('Correct', validators=[DataRequired()])
    module_code = StringField('Module Code', validators=[DataRequired()])
    incorrect_1 = StringField('Incorrect Answer 1', validators=[DataRequired()])
    incorrect_2 = StringField('Incorrect Answer 2', validators=[DataRequired()])
    incorrect_3 = StringField('Incorrect Answer 3', validators=[DataRequired()])
    difficulty = SelectField('Difficulty', choices=[('easy','easy'),('medium','medium'),('hard','hard')], validators=[DataRequired()])
    is_summative = BooleanField('Summative?')
    feedback = StringField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Upload')


class MCDeleteForm(FlaskForm):
    confirmDelete = BooleanField('Confirm:')
    submit = SubmitField('Delete')

    def validate_confirmDelete(MCDeleteForm, confirmDelete):
        confirm = confirmDelete.data
        if confirm != 1:
            raise ValidationError('Please confirm that you want to delete this question.')


def MultipleEditRoute():
    @app.route("/Edit-Multiple-Choice-Question",methods=['GET', 'POST'])
    def MultipleEdit():
        questions = Multiple.query.order_by(desc(Multiple.date_created)).all()
        return render_template("MultipleEdit.html", questions = questions)


    @app.route('/Edit-Multiple-Choice-Question/<int:id>',methods=['GET', 'POST'])
    def MultipleEditQuest(id):
        MC = db.session.query(Multiple).get(id)
        form = MCForm(obj = MC)
        if form.validate_on_submit():
            db.session.delete(MC)
            question = Multiple(id = id,
                            question=form.question.data,
                            module_code=form.module_code.data,
                            incorrect_1=form.incorrect_1.data,
                            incorrect_2=form.incorrect_2.data,
                            incorrect_3=form.incorrect_3.data,
                            correct=form.correct.data,
                            feedback=form.feedback.data,
                            difficulty=form.difficulty.data,
                            is_summative=form.is_summative.data)
            db.session.add(question)
            db.session.commit()
            flash("Changes Saved.")
            return redirect(url_for('staffhome'))
        return render_template("EditMC.html", MC=MC, form=form)


    @app.route('/Delete-Multiple-Choice-Question/<int:id>',methods=['GET', 'POST'])
    def MultipleDeleteQuest(id):

        Q1 = Assessment.query.filter_by(q1_type = "Multiple", q1_id = id).first()
        Q2 = Assessment.query.filter_by(q2_type = "Multiple", q2_id = id).first()
        Q3 = Assessment.query.filter_by(q3_type = "Multiple", q3_id = id).first()

        MC = db.session.query(Multiple).get(id)
        form = MCDeleteForm()
        if form.validate_on_submit():
            db.session.delete(MC)
            db.session.commit()
            flash("Question Deleted.")
            return redirect(url_for('staffhome'))
        return render_template("DeleteMC.html", MC=MC, Q1=Q1, Q2=Q2, Q3=Q3, form=form)


def MultipleRoute():
    @app.route("/Create-Multiple-Choice-Question", methods=['GET', 'POST'])
    def createMultipleChoiceQuestion():
        form = MCForm()
        if form.validate_on_submit():
            quest = Multiple(question=form.question.data, correct=form.correct.data, module_code=form.module_code.data, incorrect_1=form.incorrect_1.data, incorrect_2=form.incorrect_2.data, incorrect_3=form.incorrect_3.data, difficulty=form.difficulty.data, is_summative=form.is_summative.data, feedback=form.feedback.data)
            db.session.add(quest)
            db.session.commit()
            flash("Question added.")
            return redirect(url_for('staffhome'))
        return render_template('Create Multiple Choice Question.html', form = form)

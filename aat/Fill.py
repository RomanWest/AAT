from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from aat.forms import RegistrationForm, LoginForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired
from flask_wtf import FlaskForm
from aat import app, db
from aat.models import Fill, Assessment
from sqlalchemy import desc

class FillQForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
    module_code = StringField('Module', validators=[DataRequired()])
    correct = StringField('Answer', validators=[DataRequired()])
    feedback = StringField('Incorrect Answer Feedback',validators = [DataRequired()])
    is_summative = BooleanField('Is summative?')
    difficulty = SelectField('Difficulty', choices=[('easy','Easy'), ('medium', 'Medium'), ('hard', 'Hard')], validators=[DataRequired()])
    submit = SubmitField('Save')

class FillDeleteForm(FlaskForm):
    confirmDelete = BooleanField('Confirm:')
    submit = SubmitField('Delete')

    def validate_confirmDelete(FillDeleteForm, confirmDelete):
        confirm = confirmDelete.data
        if confirm != 1:
            raise ValidationError('Please confirm that you want to delete this question.')

def fillblankroute():
    @app.route("/Create-Fill-in-the-Blank",methods=['GET', 'POST'])
    def FillintheBlank():
        form = FillQForm()
        if form.validate_on_submit():
            question = Fill(question=form.question.data, 
                            module_code=form.module_code.data, 
                            correct=form.correct.data,
                            feedback=form.feedback.data,
                            difficulty=form.difficulty.data,
                            is_summative=form.is_summative.data
                            )
            db.session.add(question)
            db.session.commit()
            flash("Question added.")
            return redirect(url_for('staffhome'))

        return render_template("Fill in blank.html", form=form)

def filleditroute():
    @app.route("/Edit-Fill-in-the-Blank",methods=['GET', 'POST'])
    def FillEditList():
        questions = Fill.query.order_by(desc(-Fill.date_created)).all()
        # if request.method == 'POST':
        #     fill = db.session.query(Fill).get(request.form["delete"])
        #     db.session.delete(fill)
        #     flash("deleted question")
        #     return redirect(url_for("staffhome"))
        return render_template("Fill edit list.html", questions = questions)

    @app.route("/Edit-Fill-in-the-Blank/<int:fill_id>",methods=['GET', 'POST'])
    def FillEdit(fill_id):
        fill = db.session.query(Fill).get(fill_id)
        form = FillQForm(obj = fill)
        if form.validate_on_submit():
            db.session.delete(fill)
            question = Fill(id = fill_id,
                            question=form.question.data, 
                            module_code=form.module_code.data, 
                            correct=form.correct.data,
                            feedback=form.feedback.data,
                            difficulty=form.difficulty.data,
                            is_summative=form.is_summative.data
                            )
            db.session.add(question)
            db.session.commit()
            flash("edited successfully")
            return redirect(url_for('staffhome'))
        
        return render_template("fillEdit.html", fill=fill, form=form)
    
    @app.route("/DeleteFill/<int:fill_id>", methods=['GET', 'POST'])
    def DeleteFill(fill_id):

        Q1 = Assessment.query.filter_by(q1_type = "Fill", q1_id = fill_id).first()
        Q2 = Assessment.query.filter_by(q2_type = "Fill", q2_id = fill_id).first()
        Q3 = Assessment.query.filter_by(q3_type = "Fill", q3_id = fill_id).first()

        fill = db.session.query(Fill).get(fill_id)
        form = FillDeleteForm()
        if form.validate_on_submit():
            db.session.delete(fill)
            db.session.commit()
            return redirect(url_for('staffhome'))
        return render_template("fillDelete.html", fill=fill, Q1=Q1, Q2=Q2, Q3=Q3, form=form)


        
def test_fill_route():
    @app.route("/testFill")
    def test_fill_all():
        questions = Fill.query.order_by(desc(-Fill.date_created)).all()

        return render_template("testFillAll.html", questions=questions)

    @app.route("/testFill/<int:fill_id>", methods=['GET', 'POST'])
    def test_fill(fill_id):
        fill = db.session.query(Fill).get(fill_id)
        question = (fill.question).replace(fill.correct, "_______")

        if request.method == 'POST':
            answer = request.form.get("answer")
            if answer.lower() == fill.correct.lower():
                flash("right")
            else:
                flash(fill.feedback)

        return render_template("testFill.html", fill=fill, question=question)

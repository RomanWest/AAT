from datetime import datetime
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from flask_wtf.form import FlaskForm
from wtforms import validators
from wtforms.fields.core import DateField, DateTimeField, StringField, RadioField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from aat import app, db
from aat.models import Assessment, User, Multiple, Fill, Attempts
from aat.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from aat import app, db

# Need to look at form


class Answer_Form(FlaskForm):
    answer_1_fill = StringField('answer1')
    answer_2_fill = StringField('answer2')
    answer_3_fill = StringField('answer3')
    answer_1_multi = RadioField('answer1')
    answer_2_multi = RadioField('answer2')
    answer_3_multi = RadioField('answer3')
    submit = SubmitField('Submit')


def testassess_route():

    @app.route("/Attempt-Assessment/<int:assessment_id>", methods=['GET', 'POST'])
    def testassess(assessment_id):
        assessment = Assessment.query.get_or_404(assessment_id)
        multiple_all = Multiple.query.all()
        fill_all = Fill.query.all()
        form = Answer_Form()
        # grab the questuions from the question tables

        q1_multi = Multiple.query.filter_by(id=assessment.q1_id).first()
        q1_fill = db.session.query(Fill).get(assessment.q1_id)

        if assessment.q1_type == "Multiple":
            q1 = q1_multi.question
            correct_1 = q1_multi.correct

        else:
            q1 = (q1_fill.question).replace(q1_fill.correct, "_______")
            correct_1 = q1_fill.correct

        q2_multi = Multiple.query.filter_by(id=assessment.q2_id).first()
        q2_fill = db.session.query(Fill).get(assessment.q2_id)

        if assessment.q2_type == "Multiple":
            q2 = q2_multi.question
            correct_2 = q2_multi.correct

        else:
            q2 = (q2_fill.question).replace(q2_fill.correct, "_______")
            correct_2 = q2_fill.correct

        q3_multi = Multiple.query.filter_by(id=assessment.q3_id).first()
        q3_fill = db.session.query(Fill).get(assessment.q3_id)

        if assessment.q3_type == "Multiple":
            q3 = q3_multi.question
            correct_3 = q3_multi.correct

        else:
            q3 = (q3_fill.question).replace(q3_fill.correct, "_______")
            correct_3 = q3_fill.correct

        # Need to look at form submission
        # get the answers from the form and then put into attempts table
        form = Answer_Form()
        if request.method=="POST":
            if assessment.q1_type == "Multiple" :
                answer_1=request.form.getlist("answer_1_multi")[0]
            else:
                answer_1=form.answer_1_fill.data
        
            if assessment.q2_type == "Multiple" :
                answer_2=request.form.getlist("answer_2_multi")[0]
            else:
                answer_2=form.answer_2_fill.data
        
            if assessment.q3_type == "Multiple" :
                answer_3=request.form.getlist("answer_3_multi")[0]
            else:
                answer_3 = form.answer_3_fill.data

            answerscorrect = 0.0
            if answer_1 == correct_1:
                correct_1 = True
                answerscorrect += 1
            else:
                correct_1 = False

            if answer_2 == correct_2:
                correct_2 = True
                answerscorrect += 1
            else:
                correct_2=False

            if answer_3 == correct_3:
                correct_3 = True
                answerscorrect += 1
            else:
                correct_3 = False

            attempt = 0
            attempts = Attempts.query.filter_by(
                user_id=current_user.id, assessment_id=assessment.id).all()

            if attempts != []:
                attempt = attempts[-1].attempt_no + 1
            else:
                attempt = 1

            percentage_correct = (answerscorrect / 3) * 100
            attempt = Attempts(user_id=current_user.id, assessment_id=assessment_id,
                               answer_1=answer_1, correct_1=correct_1,
                               answer_2=answer_2, correct_2=correct_2,
                               answer_3=answer_3, correct_3=correct_3,
                               percentage_correct=percentage_correct, module_code=assessment.module_code,
                               is_summative=assessment.is_summative, attempt_no=attempt
                               )

            db.session.add(attempt)
            db.session.commit()
            flash("Assessment submitted")
            return redirect(url_for('studenthome'))

        return render_template('testassess.html', assessment=assessment,
                               multiple_all=multiple_all, fill_all=fill_all,
                               q1_multi=q1_multi, q1_fill=q1_fill, q1=q1,
                               q2_multi=q2_multi, q2_fill=q2_fill, q2=q2,
                               q3_multi=q3_multi, q3_fill=q3_fill, q3=q3,
                               form=form
                               )


class Assessment_Form(FlaskForm):
    question_1 = StringField('question-id-1', validators=[DataRequired()])
    question_2 = StringField('question-id-2', validators=[DataRequired()])
    question_3 = StringField('question-id-3', validators=[DataRequired()])
    type_1 = StringField('question-type-1', validators=[DataRequired()])
    type_2 = StringField('question-type-2', validators=[DataRequired()])
    type_3 = StringField('question-type-3', validators=[DataRequired()])
    module = StringField('module-code', validators=[DataRequired()])
    submit = SubmitField('Save')
    is_summative = StringField('assessment-type', validators=[DataRequired()])
    feedback_date = DateField('Feedback-Date')


def createassessment_route():
    @app.route("/Create-Formative", methods=['GET', 'POST'])
    def assessSubmit():
        multiple_all = Multiple.query.all()
        fill_all = Fill.query.all()
        assessment_all = Assessment.query.all()
        form = Assessment_Form()

        if request.method == "POST":
            print("Hi")
            if request.form.get('selectedType') == "Formative":
                form.is_summative.data = False
            if request.form.get('selectedType') == "Summative":
                form.is_summative.data = True

            form.module.data = request.form.getlist('selectedModule')[0]
            
            if request.form.getlist("checked!"):
                value = request.form.getlist('checked!')
                print(value)
                id_type = []
                for i in range(len(value)):
                    id_type.append(value[i].split(" "))

                print(id_type)
            createdAssessment = Assessment(q1_id=int(id_type[0][1]),
                                           q2_id=int(id_type[1][1]),
                                           q3_id=int(id_type[2][1]),
                                           q1_type=id_type[0][0],
                                           q2_type=id_type[1][0],
                                           q3_type=id_type[2][0],
                                           is_summative=form.is_summative.data,
                                           assessment_name='Testing',
                                           admin_created=True,
                                           module_code=form.module.data
                                           )
            db.session.add(createdAssessment)
            db.session.commit()
            flash("Assessment added.")
            return redirect(url_for('assessSubmit'))

        return render_template("Create Formative.html", form=form, multiple_all=multiple_all, fill_all=fill_all, assessment_all=assessment_all)

from datetime import datetime 
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField, RadioField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from aat import app, db
from aat.models import Assessment, User, Multiple, Fill, Attempts
from aat.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from aat import app, db

# Need to look at form 
class Answer_Form(FlaskForm):
        answer_1_fill = StringField('answer1', validators=[DataRequired()])
        answer_2_fill = StringField('answer2', validators=[DataRequired()])
        answer_3_fill = StringField('answer3', validators=[DataRequired()])
        answer_1_multi = RadioField('answer1', validators=[DataRequired()])
        answer_2_multi = RadioField('answer2', validators=[DataRequired()])
        answer_3_multi = RadioField('answer3', validators=[DataRequired()])
        submit = SubmitField('Submit')


def testassess_route():

    @app.route("/Attempt-Assessment/<int:assessment_id>",methods=['GET','POST'])
    def testassess(assessment_id):
        assessment = Assessment.query.get_or_404(assessment_id)
        multiple_all = Multiple.query.all()
        fill_all = Fill.query.all()
        form = Answer_Form()
        
        q1_multi = Multiple.query.filter_by(id = assessment.q1_id).first()
        q1_fill = Fill.query.filter_by(id = assessment.q1_id).first()

        if assessment.q1_type == "Multiple" :
            q1 = q1_multi
        else:
            q1 = q1_fill

        q2_multi = Multiple.query.filter_by(id = assessment.q2_id).first()
        q2_fill = Fill.query.filter_by(id = assessment.q2_id).first()

        if assessment.q2_type == "Multiple":
            q2 = q2_multi
        else:
            q2 = q2_fill

        q3_multi = Multiple.query.filter_by(id = assessment.q3_id).first()
        q3_fill = Fill.query.filter_by(id = assessment.q3_id).first()

        if assessment.q3_type == "Multiple":
            q3 = q3_multi
        else:
            q3 = q3_fill
        
        # Need to look at form submission

   

        return render_template('testassess.html', assessment=assessment, 
            multiple_all=multiple_all, fill_all=fill_all, 
            q1_multi=q1_multi, q1_fill=q1_fill, q1=q1,
            q2_multi=q2_multi, q2_fill=q2_fill, q2=q2,
            q3_multi=q3_multi, q3_fill=q3_fill, q3=q3,
            form=form
            )

    def attempt_answers():
            form = Answer_Form()
            if form.validate_on_submit():
                assessment = Assessment.query.get_or_404()
                if assessment.q1_type == "Multiple" :
                    answer_options = q1_multi
                    answer_1=form.answer_1_multi.data
                else:
                    answer_1=form.answer_1_fill.data
                
                if assessment.q2_type == "Multiple" :
                    answer_2=form.answer_2_multi.data
                else:
                    answer_2=form.answer_2_fill.data
                
                if assessment.q3_type == "Multiple" :
                    answer_3=form.answer_3_multi.data
                else:
                    answer_3=form.answer_3_fill.data


                attempt = Attempts(answer_1=answer_1, answer_2=answer_2, answer_3=answer_3)

                db.session.add(attempt)
                db.session.commit()
                flash("Assessment submitted")
                return redirect(url_for('studenthome'))
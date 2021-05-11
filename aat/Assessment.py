from datetime import datetime 
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from aat import app, db
from aat.models import Assessment, User, Multiple, Fill
from aat.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from aat import app, db

def testassess_route():


    @app.route("/Attempt-Assessment/<int:assessment_id>",methods=['GET','POST'])
    def testassess(assessment_id):
        assessment = Assessment.query.get_or_404(assessment_id)
        multiple_all = Multiple.query.all()
        fill_all = Fill.query.all()
        
        q1_multi = Multiple.query.filter_by(id = assessment.q1_id).first()
        q1_fill = Fill.query.filter_by(id = assessment.q1_id).first()

        if Assessment.q1_type == 'Multiple':
            q1 = q1_multi
        else:
            q1 = q1_fill


        q2_multi = Multiple.query.filter_by(id = assessment.q2_id).first()
        q2_fill = Fill.query.filter_by(id = assessment.q2_id).first()

        if Assessment.q2_type == 'Multiple':
            q2 = q2_multi
        else:
            q2 = q2_fill

        q3_multi = Multiple.query.filter_by(id = assessment.q3_id).first()
        q3_fill = Fill.query.filter_by(id = assessment.q3_id).first()

        if Assessment.q3_type == 'Multiple':
            q3 = q3_multi
        else:
            q3 = q3_fill

  
        print(assessment)
        return render_template('testassess.html', assessment=assessment, 
            multiple_all=multiple_all, fill_all=fill_all, 
            q1_multi=q1_multi, q1_fill=q1_fill, q1=q1,
            q2_multi=q2_multi, q2_fill=q2_fill, q2=q2,
            q3_multi=q3_multi, q3_fill=q3_fill, q3=q3
            )

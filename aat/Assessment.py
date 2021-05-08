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
        # questionQuery1 = (db.session.query(Assessment)
        #     .join(Multiple)
        #     .filter(Multiple.id.in_(Assessment.id)))
            
            # .filter_by(id=Assessment.q1_id).all())
        
    #     if Assessment.q1_type == 'Multiple':
    #         #looking_for = 'Multiple'
    #         questionQuery1 = db.session.query(Assessment, Multiple).join(Multiple).filter_by(Multiple.id)
    #         # questionQuery1 = (db.session.query(Multiple)
    #         #     .join(Assessment)
    #         #     .filter(Assessment.q1_id.in_(Multiple.id)))
    #     else:
    #         #looking_for = 'Fill'
    #         # questionQuery1 = (db.session.query(Fill)
    #         #     .join(Assessment)
    #         #     .filter(Assessment.q1_id.in_(Fill.id)))
    #         questionQuery1 = db.session.query(Assessment, Fill).join(Fill).filter_by(Fill.id)


    #    # if looking_for 

    #   #  Assessment.query.filter(Assessment.q1_type.contains(looking_for))

    #     print(questionQuery1)
        
        # for ( i < length of assessment):
        #     questions.append ( q1_type.query.filter_by (q1_id) )

        # q1_type = Assessment.query.get_or_404(q1_type)
        # q1_id = Assessment.query.get_or_404(q1_id)
        # q2_type = Assessment.query.get_or_404(q2_type)
        # q2_id = Assessment.query.get_or_404(q2_id)
        # q3_type = Assessment.query.get_or_404(q3_type)
        # q3_id = Assessment.query.get_or_404(q3_id)  
        print(assessment)
        return render_template('testassess.html', assessment=assessment, multiple_all=multiple_all, fill_all=fill_all)

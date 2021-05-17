from datetime import datetime
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from aat import app, db
from aat.models import Assessment, User, Multiple, Fill
from aat.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from aat.testroute import test
from aat.MultipleChoice import MultipleRoute, MultipleEditRoute
from aat.Fill import filleditroute, fillblankroute, test_fill_route
from aat.Assessment import testassess_route

@app.route("/Staff-Home", methods=["GET", 'POST'])
def staffhome():
    assessment_all = Assessment.query.all()
    return render_template('Staff Home.html', assessment_all=assessment_all)

@app.route("/Student-Home", methods=["GET", 'POST'])
def studenthome():
    assessment_all = Assessment.query.all()
    return render_template("Student Home.html", assessment_all=assessment_all)

@app.route("/", methods=["GET", "POST"])
@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
        login_user(user)
        flash('Login successful!')
        if user.is_admin:
            return redirect(url_for('staffhome'))
        else:
            return redirect(url_for("studenthome"))
    else:
        flash("Email or password is incorrect")
  return render_template('login.html',title='Login',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('staffhome'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('Logout successful!')
    return redirect(url_for('login'))

#for fill in blank questions:
fillblankroute()
filleditroute()
test_fill_route()


MultipleRoute()
MultipleEditRoute()

testassess_route()

@app.route("/Create-Formative")
def createFormative():
    multiple_all = Multiple.query.all()
    fill_all = Fill.query.all()
    return render_template('Create Formative.html', multiple_all=multiple_all, fill_all=fill_all)

@app.route("/Create-Summative")
def createSummative():
    multiple_all = Multiple.query.all()
    fill_all = Fill.query.all()
    return render_template('Create Summative.html', multiple_all=multiple_all, fill_all=fill_all)

@app.route("/Student-View-Progress")
def studentViewProgress():
    return render_template('Student View Progress.html')

@app.route("/Student-View-Attempts")
def studentViewAttempts():

    return render_template('Student View Attempts.html')

@app.route("/View-Quiz-Attempt")
def viewQuizAttempt():
    return render_template('View Quiz Attempt.html')

@app.route("/Generate-Quiz")
def generateQuiz():
    return render_template('Generate Quiz.html')

@app.route("/Attempt-Assessment")
def attemptAssessment():
    return render_template('Attempt Assessment.html')

@app.route("/View-Cohort")
def viewCohort():
    return render_template('View Cohort.html')

@app.route("/View-Student")
def viewStudent():
    return render_template('View Student.html')


@app.route("/Create-Question")
def createQuestion():
    return render_template('Create Question.html')


@app.route("/Preview-Assessment")
def previewAssessment():
    return render_template('Preview Assessment.html')

@app.route("/Submit-Assessment")
def submitAssessment():
    return render_template('Submit Assessment.html')
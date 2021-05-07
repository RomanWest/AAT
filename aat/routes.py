from datetime import datetime
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from aat import app, db, wildcardroute, testroute
from aat.models import User, Multiple, Fill
from aat.forms import RegistrationForm, LoginForm, FillQForm
from flask_login import login_user, logout_user, login_required, current_user
from aat.testroute import test
# from aat.Fillinblankroute import fillblankroute
#from aat.MultipleChoice import MCForm
#from aat import wildcardroute

@app.route("/Staff-Home")
def staffhome():
    return render_template('Staff Home.html')

@app.route("/Student-Home", methods=["GET", 'POST'])
def studenthome():
    test()
    return render_template("Student Home.html")

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

@app.route("/Create-Formative")
def createFormative():
    return render_template('Create Formative.html')

@app.route("/Student-View-Progress")
def studentViewProgress():
    return render_template('Student View Progress.html')

@app.route("/Student-View-Attempts")
def studentViewAttempts():
    return render_template('Student View Attempts.html')

@app.route("/View-Quiz-Attempt")
def viewQuizAttempt():
    return render_template('View Quiz Attempt.html')

#modules = ["cmt120","cmt119","cmt219"]

#@app.route("/Generate-Quiz",methods = ["GET","POST"])
#def generateQuiz():
	#return render_template("Generate Quiz.html",modules = modules)

@app.route("/Attempt-Assessment")
def attemptAssessment():
    return render_template('Attempt Assessment.html')

@app.route("/View-Cohort")
def viewCohort():
    return render_template('View Cohort.html')

@app.route("/View-Student")
def viewStudent():
    return render_template('View Student.html')

@app.route("/Create-Summative")
def createSummative():
    return render_template('Create Summative.html')

@app.route("/Create-Question")
def createQuestion():
    return render_template('Create Question.html')

@app.route("/Create-Fill-in-the-Blank", methods=['GET', 'POST'])
def FillintheBlank():
    form = FillQForm()
    if form.validate_on_submit():
        question = Fill(question=form.question.data,
                        module_code=form.module.data,
                        correct=form.answer.data,
                        feedback=form.incorrectfeedback.data,
                        difficulty=form.difficulty.data,
                        is_summative=form.issummative.data
                        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('staffhome'))

    return render_template("Fill in blank.html", form=form)


@app.route("/Create-Multiple-Choice-Question", methods=['GET', 'POST'])
def createMultipleChoiceQuestion():
    form = MCForm()
    if form.validate_on_submit():
        quest = Multiple(question=form.question.data, correct=form.correct.data, module_code=form.module_code.data, incorrect_1=form.incorrect_1.data, incorrect_2=form.incorrect_2.data, incorrect_3=form.incorrect_3.data, difficulty=form.difficulty.data, is_formative=form.is_formative.data, feedback=form.feedback.data)
        db.session.add(quest)
        db.session.commit()
        return redirect(url_for('staffhome'))
    return render_template('Create Multiple Choice Question.html', form = form)

@app.route("/Preview-Assessment")
def previewAssessment():
    return render_template('Preview Assessment.html')

@app.route("/Submit-Assessment")
def submitAssessment():
    return render_template('Submit Assessment.html')

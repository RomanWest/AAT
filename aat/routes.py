from datetime import datetime
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from aat import app, db
from aat.models import Assessment, User, Multiple, Fill, Attempts
from aat.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from aat.testroute import test
from aat.MultipleChoice import MultipleRoute, MultipleEditRoute
from aat.Fill import filleditroute, fillblankroute, test_fill_route
from aat.Assessment import Assessment_Form, createassessment_route, testassess_route


@app.route("/c")
@app.route("/Staff-Home", methods=["GET", 'POST'])
def staffhome():
    assessment_all = Assessment.query.all()

    return render_template('Staff Home.html', assessment_all=assessment_all)


@app.route("/Delete-Assessment/<int:assessment_id>", methods=['GET', 'POST'])
def DeleteAssessment(assessment_id):
    assessment = db.session.query(Assessment).get(assessment_id)
    if request.method == 'POST':

        if request.form.get("delete"):
            db.session.delete(assessment)
            db.session.commit()
            flash("Assessment deleted.")
            return redirect(url_for("staffhome"))

        if request.form.get("keep"):
            return redirect(url_for("staffhome"))

    return render_template("AssessmentDelete.html", assessment=assessment)


@app.route("/Student-Home", methods=["GET", 'POST'])
def studenthome():
    assessment_all = Assessment.query.all()
    return render_template("Student Home.html", assessment_all=assessment_all)


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=['GET', 'POST'])
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
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, first_name=form.first_name.data,
                    last_name=form.last_name.data, email=form.email.data, password=form.password.data)
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


# for fill in blank questions:
fillblankroute()
filleditroute()
test_fill_route()


MultipleRoute()
MultipleEditRoute()

testassess_route()

createassessment_route()


@app.route("/Create-Summative", methods=['GET', 'POST'])
def assessSubmit2():
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

        form.module_code.data = request.form.getlist('selectedModule')[0]

        if request.form.getlist("checked!"):
            value = request.form.getlist('checked!')
            id_type = []
            for i in range(len(value)):
                id_type.append(value[i].split(" ", 2))
            print("tim")
            print(id_type)
            print(id_type[0][2])
        createdAssessment = Assessment(q1_id=int(id_type[0][1]),
                                           q2_id=int(id_type[1][1]),
                                           q3_id=int(id_type[2][1]),
                                           q1_type=id_type[0][0],
                                           q2_type=id_type[1][0],
                                           q3_type=id_type[2][0],
                                           q1_feedback=id_type[0][2],
                                           q2_feedback=id_type[1][2],
                                           q3_feedback=id_type[2][2],
                                           is_summative=form.is_summative.data,
                                           assessment_name=form.assessment_name.data,
                                           admin_created=True,
                                           module_code=form.module_code.data
                                           )
        db.session.add(createdAssessment)
        db.session.commit()
        flash("Assessment added.")
        return redirect(url_for('assessSubmit2'))

    return render_template("Create Summative.html", form=form,
                               multiple_all=multiple_all, fill_all=fill_all,
                               assessment_all=assessment_all)


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
    return render_template('View Attempt.html')


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


@app.route('/View-Student-Number')
def viewStudentNumber():
    post = User.query(db.func.count(User.is_admin == False)).all()
    return render_template('View Student Number.html', post=post)


@app.route('/View-Student-List')
def viewStudentList():
    post = User.query.all()
    return render_template('View Student List.html', post=post)


@app.route('/Search-Student')
def searchStudent():
    #post = User.query.filter(User.id == ('%{keyword}%'.format(keyword=request.form.get('search_input')))).all()
    return render_template("View Student Search.html")


@app.route('/View-Attempts')
def viewAttempts():
    post = Attempts.query.all()
    return render_template("View Attempt.html", post=post)


@app.route("/Edit-Assessment/<int:assessment_id>", methods=['GET', 'POST'])
def EditAssessment(assessment_id):
    multiple_all = Multiple.query.all()
    fill_all = Fill.query.all()
    assessment = db.session.query(Assessment).get(assessment_id)
    form = Assessment_Form(formdata=request.form, obj=assessment)

    if request.method == "POST":

        if request.form.getlist("checked!"):
            value = request.form.getlist('checked!')
            id_type = []
            for i in range(len(value)):
                id_type.append(value[i].split(" ", 2))

        if request.form.get('selectedType') == "Formative":
            form.is_summative.data = False
        if request.form.get('selectedType') == "Summative":
            form.is_summative.data = True

        moduleCode = request.form.get('moduleCode')
        print(moduleCode)

        db.session.delete(assessment)
        assessment_edit = Assessment(id=assessment_id,
                                     q1_id=int(id_type[0][1]),
                                     q2_id=int(id_type[1][1]),
                                     q3_id=int(id_type[2][1]),
                                     q1_type=id_type[0][0],
                                     q2_type=id_type[1][0],
                                     q3_type=id_type[2][0],
            q1_feedback=id_type[0][2],
            q2_feedback=id_type[1][2],
            q3_feedback=id_type[2][2],
            module_code=moduleCode,  # Needs changing
            is_summative=form.is_summative.data,
            assessment_name=form.assessment_name.data
        )

        print(assessment_edit)
        db.session.add(assessment_edit)
        db.session.commit()
        flash("edited successfully")
        return redirect(url_for('staffhome'))
    return render_template('Edit Assessment.html', assessment=assessment, form=form, multiple_all=multiple_all, fill_all=fill_all)

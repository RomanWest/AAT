from aat import app, db
from aat.models import User, Multiple, Fill
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
import random

class random_Form(FlaskForm):
    q1 = StringField('answer')
    q2 = StringField('answer')
    q3 = StringField('answer')


rand_questions = []


@app.route("/Generate-Quiz",methods = ["GET","POST"])
def generateQuiz():
	user = User.query.limit(1).all()
	#user2 = flask_login.current_user
	#print(user2)
	return render_template("Generate Quiz.html",user = user)

@app.route("/random",methods = ["POST"])
def Random():
	rand_questions.clear()
	form = random_Form()
	Q1_module = request.form["Q1_module"]
	Q1_diff = request.form["Q1_diff"]
	Q2_module = request.form["Q2_module"]
	Q2_diff = request.form["Q2_diff"]
	Q3_module = request.form["Q3_module"]
	Q3_diff = request.form["Q3_diff"]
	Q1 = [Q1_module,Q1_diff]
	Q2 = [Q2_module,Q2_diff]
	Q3 = [Q3_module,Q3_diff]
	data = [Q1,Q2,Q3]
	MCQ1 = []
	MCQ2 = []
	MCQ3 = []
	MCQ = [MCQ1,MCQ2,MCQ3]
	current_mcq = []
	for i in range(0,3):
		rand = random.randint(1,2)
		if (rand == 1):
			q = getMLC(data[i][0],data[i][1],rand_questions)
			rand_questions.append("MCQ")
			rand_questions.append(q)
			current_mcq.append(q.correct)
			current_mcq.append(q.incorrect_1)
			current_mcq.append(q.incorrect_2)
			current_mcq.append(q.incorrect_3)
			random.shuffle(current_mcq)
			MCQ[i] = MCQ[i] + current_mcq
			current_mcq.clear()
		else:
			q = getFill(data[i][0],data[i][1],rand_questions)
			rand_questions.append("Fill")
			rand_questions.append(q)
	return render_template('random.html',data = data,questions = rand_questions,MCQ=MCQ,form=form)




#Fill = [F1,F2,F3,F4,F5,F6]

def getMLC(code,diff,list):
	mcq = Multiple.query.all()
	#print(mcq)
	data = []
	for i in mcq:
		#print(isinstance(i,Multiple))
		if ((i.module_code == code) and (i.difficulty == diff) and (i not in list) and (i.is_summative == False)):
			data.append(i)
	#print(data)
	#if data size = 0, call getfill?
	#print(data)
	rand = random.randint(1,len(data))
	return data[rand - 1]

def getFill(code,diff,list):
	f = Fill.query.all()
	#print(f)
	data = []
	for i in f:
		if ((i.module_code == code) and (i.difficulty == diff) and (i not in list) and (i.is_summative == False)):
			data.append(i)
	#print(data)
	rand = random.randint(1,len(data))
	return data[rand - 1]

@app.route("/randomResults",methods = ["POST"])
def randomResults():
	rand_q1 = request.form.get("q1")
	rand_q2 = request.form.get("q2")
	rand_q3 = request.form.get("q3")
	data = [rand_q1,rand_q2,rand_q3]
	correct = [rand_questions[1].correct,rand_questions[3].correct,rand_questions[5].correct]
	feedback = [rand_questions[1].feedback,rand_questions[3].feedback,rand_questions[5].feedback]
	names = [rand_questions[1].question,rand_questions[3].question,rand_questions[5].question]
	score = 0
	for i in range(0,len(data)):
		if (data[i] == correct[i]):
			score += 1
	#questions.clear()
	return render_template('randomResults.html',data=data,correct=correct, score=score, feedback= feedback,names=names)

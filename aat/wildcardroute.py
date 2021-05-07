from aat import app, db
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
import random


modules = ["cmt120","cmt119","cmt219"]

@app.route("/Generate-Quiz",methods = ["GET","POST"])
def generateQuiz():
	return render_template("Generate Quiz.html",modules = modules)

@app.route("/random",methods = ["POST"])
def Random():
	Q1_module = request.form["Q1_module"]
	Q1_diff = request.form["Q1_diff"]
	Q2_module = request.form["Q2_module"]
	Q2_diff = request.form["Q2_diff"]
	Q1 = [Q1_module,Q1_diff]
	Q2 = [Q2_module,Q2_diff]
	data = [Q1,Q2]
	questions = []
	for i in range(0,2):
		rand = random.randint(1,2)
		if (rand == 1):
			q = getMLC(data[i][0],data[i][1],questions)
			questions.append(q)
		else:
			q = getFill(data[i][0],data[i][1],questions)
			questions.append(q)
	#print(questions)
	return render_template('random.html',data = data,questions = questions)



M1 ={"id":1,"code":"cmt120","difficulty":"easy","is_formative":True,"type":"MLC"}
M2 ={"id":2,"code":"cmt120","difficulty":"medium","is_formative":True,"type":"MLC"}
M3 ={"id":3,"code":"cmt120","difficulty":"hard","is_formative":True,"type":"MLC"}
M4 ={"id":4,"code":"cmt120","difficulty":"easy","is_formative":True,"type":"MLC"}
M5 ={"id":5,"code":"cmt120","difficulty":"medium","is_formative":True,"type":"MLC"}
M6 ={"id":6,"code":"cmt120","difficulty":"hard","is_formative":True,"type":"MLC"}

F1 ={"id":1,"code":"cmt120","difficulty":"easy","is_formative":True,"type":"Fill"}
F2 ={"id":2,"code":"cmt120","difficulty":"medium","is_formative":True,"type":"Fill"}
F3 ={"id":3,"code":"cmt120","difficulty":"hard","is_formative":True,"type":"Fill"}
F4 ={"id":4,"code":"cmt120","difficulty":"easy","is_formative":True,"type":"Fill"}
F5 ={"id":5,"code":"cmt120","difficulty":"medium","is_formative":True,"type":"Fill"}
F6 ={"id":6,"code":"cmt120","difficulty":"hard","is_formative":True,"type":"Fill"}

MLC = [M1,M2,M3,M4,M5,M6]
Fill = [F1,F2,F3,F4,F5,F6]

def getMLC(code,diff,list):
	data = []
	for i in MLC:
		if ((i["code"] == code) and (i["difficulty"] == diff) and (i not in list) and (i["is_formative"] == True)):
			data.append(i)
	#print(data)
	rand = random.randint(1,len(data))
	return data[rand - 1]

def getFill(code,diff,list):
	data = []
	for i in Fill:
		if ((i["code"] == code) and (i["difficulty"] == diff) and (i not in list)):
			data.append(i)
	#print(data)
	rand = random.randint(1,len(data))
	return data[rand - 1]

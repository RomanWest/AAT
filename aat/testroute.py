from aat import app, db
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
def test():
    if request.method == 'POST':
        print("hi")

modules = ["cmt120","cmt119","cmt219"]


@app.route("/generate",methods = ["GET","POST"])
def generate():
	return render_template("generate.html",modules = modules)

question = ["correct","incorrect","incorrect","incorrect"]
question2 = ["incorrect","correct","incorrect","incorrect"]
question3 = ["incorrect","incorrect","correct","incorrect"]
question4 = ["incorrect","incorrect","incorrect","correct"]
module1 = [question, question2]
module2 = [question3,question3]
category = [module1,module2]
#dict ?



@app.route("/random",methods = ["POST"])
def random():	
	Q1_module = request.form["Q1_module"]
	Q1_diff = request.form["Q1_diff"]
	Q2_module = request.form["Q2_module"]
	Q2_diff = request.form["Q2_diff"]
	Q1 = [Q1_module,Q1_diff]
	Q2 = [Q2_module,Q2_diff]
	data = [Q1,Q2]	
	return render_template('random.html',data = data)
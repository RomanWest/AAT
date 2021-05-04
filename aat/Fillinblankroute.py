# from flask import render_template, url_for, request, redirect, flash, g, current_app, session
# from aat.forms import RegistrationForm, LoginForm, FillQForm
# from aat import app, db
# from aat.models import Fill



# def fillblankroute():
#     @app.route("/Create-Fill-in-the-Blank",methods=['GET', 'POST'])
#     def FillintheBlank():
#         form = FillQForm()
#         if form.validate_on_submit():
#             question = Fill(question=form.question.data, 
#                             module_code=form.module.data, 
#                             correct=form.answer.data,
#                             feedback=form.incorrectfeedback.data,
#                             difficulty=form.difficulty.data,
#                             is_summative=form.issummative.data
#                             )
#             db.session.add(question)
#             db.session.commit()
#             return redirect(url_for('staffhome'))

#         return render_template("Fill in blank.html", form=form)

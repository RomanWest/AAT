from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from aat.forms import RegistrationForm, LoginForm, FillQForm
from aat import app, db
from aat.models import Fill
from sqlalchemy import desc


def filleditroute():
    @app.route("/Edit-Fill-in-the-Blank",methods=['GET', 'POST'])
    def FillEditList():
        questions = Fill.query.order_by(desc(-Fill.date_created)).all()
        return render_template("Fill edit list.html", questions = questions)

    @app.route("/Edit-Fill-in-the-Blank/<int:fill_id>",methods=['GET', 'POST'])
    def FillEdit(fill_id):
        fill = db.session.query(Fill).get(fill_id)
        form = FillQForm(formdata=request.form, obj = fill)
        if form.validate_on_submit():
            db.session.delete(fill)
            question = Fill(question=form.question.data, 
                            module_code=form.module_code.data, 
                            correct=form.correct.data,
                            feedback=form.feedback.data,
                            difficulty=form.difficulty.data,
                            is_summative=form.is_summative.data
                            )
            db.session.add(question)
            db.session.commit()
            flash("edited successfully")
            return redirect(url_for('staffhome'))
        return render_template("fillEdit.html", fill=fill, form=form)

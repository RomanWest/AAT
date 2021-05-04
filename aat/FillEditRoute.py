from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from aat.forms import RegistrationForm, LoginForm, FillQForm
from aat import app, db
from aat.models import Fill
from sqlalchemy import desc




def filleditroute():
    @app.route("/Edit-Fill-in-the-Blank",methods=['GET', 'POST'])
    def FillEdit():
        questions = Fill.query.order_by(desc(Fill.date_created)).all()
        return render_template("Fill Edit.html", questions = questions)

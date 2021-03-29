from datetime import datetime
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
from aat import app, db
from aat.models import User
from aat.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
<<<<<<< HEAD
=======

>>>>>>> a479c7a1d00e13765c2159bd213b302572f60edd
 
@app.route("/home") 
def home():
    return render_template('home.html')

@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
        login_user(user)
        flash('Login successful!')
        return redirect(url_for('home'))
    else:
        flash("Email or password is incorrect")
  return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('Logout successful!')
    return redirect(url_for('home'))
from aat import app, db
from flask import render_template, url_for, request, redirect, flash, g, current_app, session
def test():
    if request.method == 'POST':
        print("hi")


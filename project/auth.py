from flask import Flask, Blueprint, render_template, request, flash
from . import db


auth = Blueprint('auth', __name__)
app = Flask(__name__, static_url_path='/static')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        Name = request.form.get('name')
        password = request.form.get('password')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(Name) < 2:
            flash('Name must be greater than 1 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            #add user to the database
            flash('Account created succesfully!', category='success')
    return render_template('sign_up.html')
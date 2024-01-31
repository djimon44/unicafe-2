from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Inventory, Note  # Assuming your model is defined in the models.py file
from . import db  # Import the database instance
import os
from flask_sqlalchemy import SQLAlchemy
import sqlite3

ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])

views = Blueprint('views', __name__)
app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = '/home/dimitri/code-wsl/gdv-project/project/static/uploads'

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', user=current_user)

@views.route('/note', methods=['POST'])
@login_required
def note():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        data = request.form.get('data')

        new_note = Note(name=name, email=email, mobile=mobile, data=data, user=current_user)
        db.session.add(new_note)
        db.session.commit()

    return render_template('index.html', user=current_user)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@views.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    # Connect to SQLite3 database
    conn = sqlite3.connect('/home/dimitri/code-wsl/gdv-project/instance/database.db')  # Replace with your database name
    cursor = conn.cursor()

    # Execute a SELECT query to fetch data from the table
    cursor.execute('SELECT * FROM Inventory')  # Replace with your table name
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    return render_template('order.html', data=data)

@views.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        name = request.form.get('name')
        caption = request.form.get('caption')
        price = request.form.get('price')
        picture = request.files.get('picture')

        picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture.filename)
        picture.save(picture_path)

        # Save data to the Inventory table using Flask-SQLAlchemy
        new_item = Inventory(name=name, caption=caption, price=price, picture=picture_path)
        db.session.add(new_item)
        db.session.commit()

    return render_template('inventory.html')

@views.route('/comments', methods=['GET', 'POST'])
@login_required
def comments():
    # Connect to SQLite3 database
    conn = sqlite3.connect('/home/dimitri/code-wsl/gdv-project/instance/database.db')  # Replace with your database name
    cursor = conn.cursor()

    # Execute a SELECT query to fetch data from the table
    cursor.execute('SELECT * FROM Note')  # Replace with your table name
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    return render_template('comments.html', data=data)
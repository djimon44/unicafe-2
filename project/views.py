from flask import Flask, Blueprint, render_template
from . import db

views = Blueprint('views', __name__)
app = Flask(__name__, static_url_path='/static')

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@views.route('/profile', methods=['GET', 'POST'])
def home1():
    return render_template('profile.html')



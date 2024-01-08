from flask import Flask, Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)
app = Flask(__name__, static_url_path='/static')

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', user=current_user)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)



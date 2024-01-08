from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)

    migrate = Migrate(app, db)

    app.config['SECRET_KEY'] = '12345'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
  
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .views import views as main_blueprint
    app.register_blueprint(main_blueprint)

    from .models import User, Note

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_login import LoginManager
from .auth.models import User
from flask_marshmallow import Marshmallow




db = SQLAlchemy()

login_manager = LoginManager()

ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')


    app.config.from_object(Config)
    
    
    db.init_app(app)
    login_manager.init_app(app)
    ma.init_app(app)


    @login_manager.user_loader

    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():


        from .auth import auth
        from .cars import cars

        app.register_blueprint(auth)
        app.register_blueprint(cars)
    
    return app



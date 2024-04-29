from os import path

from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from honeybadger.contrib import FlaskHoneybadger

db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bilalai'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['HONEYBADGER_ENVIRONMENT'] = 'production'
    app.config['HONEYBADGER_API_KEY'] = 'hbp_jeX8oErG7uxSBA5EreGhcT6PqbgUVM2GwU73'
    app.config['HONEYBADGER_PARAMS_FILTERS'] = 'password, secret, credit-card'
    FlaskHoneybadger(app, report_exceptions=True)
    db.init_app(app)
   
    from .auth import auth
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
   
    create_database(app)
   
    return app
def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Created Database!')

from flask import Flask
from .models import db
from .routes import main_routes

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '500bb0f9-92b3-4523-a866-903255ca03ec'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:alfombra@localhost/projekt'
    
    db.init_app(app)

    app.register_blueprint(main_routes)

    return app


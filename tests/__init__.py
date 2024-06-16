# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
from pathlib import Path

# Añade el directorio del proyecto al PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parents[1]))

# Importa directamente desde la ruta correcta de tu proyecto
from app.routes import main_routes

db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Configuración de la aplicación según config_name (development, testing, production, etc.)
    app.config.from_object(config_name)
    
    # Configurar la base de datos
    db.init_app(app)
    
    # Registrar blueprints (rutas)
    from app.routes import main_routes
    app.register_blueprint(main_routes)
    
    return app



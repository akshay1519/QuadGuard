# app/__init__.py

from flask import Flask
from app.controllers.cpu_health_controller import cpu_health_controller
from app.controllers.main_controller import main_controller
from app.controllers.backup_controller import backup_controller
from app.controllers.config_controller import config_controller
from app.controllers.password_controller import password_controller

# app/__init__.py

from flask import Flask
from .controllers.cpu_health_controller import cpu_health_controller
from .controllers.main_controller import main_controller

def create_app():
    app = Flask(__name__)
    app.register_blueprint(cpu_health_controller)
    app.register_blueprint(main_controller)
    app.register_blueprint(backup_controller)
    app.register_blueprint(config_controller)
    app.register_blueprint(password_controller)
    
    return app
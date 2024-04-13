from flask import render_template,Blueprint
from app.config import DATABASE_CONFIG, SERVER_CONFIG

config_controller = Blueprint('config_controller', __name__)

@config_controller.route('/config', methods=['GET'])
def config():
    return render_template('config.html', database_config=DATABASE_CONFIG, server_config=SERVER_CONFIG)
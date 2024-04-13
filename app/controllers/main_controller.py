# app/controllers/main_controller.py

from flask import Blueprint, render_template

main_controller = Blueprint('main_controller', __name__)

@main_controller.route('/')
@main_controller.route('/index')
def index():
    return render_template('index.html', title='Home')
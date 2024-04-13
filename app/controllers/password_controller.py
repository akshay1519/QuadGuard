from flask import render_template,Blueprint,request
from app.models.password import Password

password_controller = Blueprint('password_controller', __name__)

@password_controller.route('/password')
def password():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        text = request.form['text']
        print(text)
        password_generator = Password()
        password = password_generator.check_password_strength(text)
        return f"<h1>{password}</h1>"


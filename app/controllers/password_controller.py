from flask import render_template,Blueprint,request
from app.models.password import Password

password_controller = Blueprint('password_controller', __name__)

@password_controller.route('/password', methods=['GET','POST'])
def password():
    return render_template('password.html')

@password_controller.route('/validatepassword', methods=['POST'])
def validate_password():
    if request.method == 'POST':
        password = request.form['password']
        password_instance = Password()
        errors = password_instance.check_password_strength(password)
        if len(errors) == 0:
            errors.append("your password meets the required criteria")
            return render_template('password.html', success=errors[0])
        else:
            return render_template('password.html', errors=errors)
    else:
        return render_template('password.html')

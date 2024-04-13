from flask import Blueprint, render_template,jsonify , current_app
from app.models.cpu_health import CpuHealth

cpu_health_controller = Blueprint('cpu_health_controller', __name__)

@cpu_health_controller.route('/cpustatus', methods=['GET'])
def cpu_health():
    return render_template('cpustatus.html')

@cpu_health_controller.route('/start_monitoring', methods=['POST'])
def start_monitoring():
    if 'cpu_health' not in current_app.extensions:
        current_app.extensions['cpu_health'] = CpuHealth()
    cpu_health = current_app.extensions['cpu_health']
    cpu_health.start_monitoring()
    return jsonify({'message': 'Monitoring started'})

@cpu_health_controller.route('/stop_monitoring', methods=['POST'])
def stop_monitoring():
    if 'cpu_health' in current_app.extensions:
        cpu_health = current_app.extensions['cpu_health']
        cpu_health.stop_monitoring()
    return jsonify({'message': 'Monitoring stopped'})

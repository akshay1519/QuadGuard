from flask import Blueprint, render_template 
from app import socketio
from app.models.cpu_health import cpu_health

cpu_health_controller = Blueprint('cpu_health_controller', __name__)
cpu_health_instance = cpu_health(socketio)

@cpu_health_controller.route('/cpustatus', methods=['GET'])
def cpu_health_status():
    return render_template('cpustatus.html')

@socketio.on('start_monitoring')
@cpu_health_controller.route('/start_monitoring')
def start_monitoring():
    cpu_health_instance.start_monitoring()
    socketio.send('Monitoring started')

@socketio.on('stop_monitoring')
@cpu_health_controller.route('/stop_monitoring')
def stop_monitoring():
    cpu_health_instance.stop_monitoring()
    socketio.send('Monitoring stopped')
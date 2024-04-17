import time
import psutil
from threading  import Thread

class cpu_health :
    def __init__(self, socketio):
        self.socketio = socketio
        self.thread = None
        self.exit_program = False
        self.monitoring = False

    def monitor(self):
        while not self.exit_program:
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
            except Exception as e:
                print(f"Error occured while monitoring cpu usage: {e}")
                continue

            message = ""
            if cpu_usage >= 90:
                message = "Alert! CPU usage exceeds threshold: 90%"
            elif cpu_usage >= 85:
                message = "Alert! CPU usage exceeds threshold: 85%"
            else:
                message = f"Monitoring CPU usage... {cpu_usage}%"

            print('Emitting message:', message)
            self.socketio.emit('cpu_usage', {'data': message})
            time.sleep(0.1)
            

    def start_monitoring(self):
        if not self.monitoring:
            self.monitoring = True    
            self.exit_program = False
            if self.thread is None or not self.thread.is_alive():
                self.thread = Thread(target=self.monitor)
                self.thread.start()
            print('Monitoring started')
    
    def stop_monitoring(self):
        if self.monitoring:
            self.monitoring = False
            self.exit_program = True
            if self.thread is not None:
                self.thread.join()
                self.socketio.emit('cpu_usage', {'data': 'Monitoring stopped'})
                self.thread = None
            print('Monitoring stopped')

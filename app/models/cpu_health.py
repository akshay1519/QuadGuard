import socket
import psutil
import threading

class CpuHealth:
    def __init__(self, host='localhost', port=5000):
        self.exit_program = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))  # 

    def monitor(self):
        while not self.exit_program:
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
            except Exception as e:
                print(f"Error occured while monitoring cpu usage: {e}")
                continue

            message = "Monitoring CPU usage..."
            if cpu_usage >= 90:
                message = "Alert! CPU usage exceeds threshold: 90%"
            elif cpu_usage >= 85:
                message = "Alert! CPU usage exceeds threshold: 85%"

            print(message)
            self.sock.sendall(message.encode())

    def start_monitoring(self):
        try:
            self.exit_program = False
            self.thread = threading.Thread(target=self.monitor)
            self.thread.start()
        except Exception as e:
            print(f"Error occurred while starting monitoring: {e}")

    def stop_monitoring(self):
        try:
            self.exit_program = True
            self.thread.join()
        except Exception as e:
            print(f"Error occurred while stopping monitoring: {e}")
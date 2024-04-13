# app/controllers/backup_controller.py

from flask import Blueprint, render_template
from app.models.backup import Backup

backup_controller = Blueprint('backup_controller', __name__)

@backup_controller.route('/backup')
def backup():
    backups = Backup.query.all()
    return render_template('backup.html', backups=backups)
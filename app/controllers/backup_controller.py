from flask import Blueprint, render_template, request
from app.models.backup import Backup

backup_controller = Blueprint('backup_controller', __name__)

@backup_controller.route('/backup', methods=['GET','POST'])
def backup():
    if request.method == 'POST':
        print(request.form)
        source_dir = request.form['source_dir_path']
        dest_dir = request.form['dest_dir_path']
        print(f'Source directories: {source_dir}')
        print(f'Destination directory: {dest_dir}')
        backup_instance = Backup(source_dir, dest_dir)
        try:
            backup_instance.run_backup()
            message = 'Backup completed successfully'
        except Exception as e:
            message = f'Error: {e}'
        return render_template('backup.html', message=message)
    else:
        return render_template('backup.html')
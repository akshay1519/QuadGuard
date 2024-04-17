import os
import shutil
import datetime

class Backup:
    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir

    def run_backup(self):
        # Check if source directory exists
        if not os.path.exists(self.source_dir):
            print("Source directory does not exist.")
            return

        # Check if destination directory exists
        if not os.path.exists(self.destination_dir):
            print("Destination directory does not exist.")
            return

        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        # Copy the files from source directory to destination directory
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                source_file = os.path.join(root, file)
                destination_file = os.path.join(self.destination_dir, file)

                # Check if destination file already exists
                if os.path.exists(destination_file):
                    # Append timestamp to file name
                    file_name, file_ext = os.path.splitext(file)
                    destination_file = os.path.join(self.destination_dir, file_name + "_" + timestamp + file_ext)

                shutil.copy2(source_file, destination_file)

        print("Backup completed successfully!")

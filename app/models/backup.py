import sys
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

        # for root, dirs, files in os.walk(self.source_dir):
        #     print(f"Root: {root}")
        #     print(f"Directories: {dirs}")
        #     print(f"Files: {files}")

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

# # Take input from user for source directory and destination directory
# if len(sys.argv) != 3:
#     print("Command: python backup.py <source_dir> <destination_dir>")
#     sys.exit(1)

# source_dir = sys.argv[1]
# destination_dir = sys.argv[2]
# backup = Backup(source_dir, destination_dir)
# backup.run_backup()
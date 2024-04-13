import configparser
import os

#Get all the path to the config file
config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')

#Read and parse the config file
config = configparser.ConfigParser()
config.read(config_file_path)

#Export the config object
DATABASE_CONFIG = dict(config['Database'])
SERVER_CONFIG = dict(config['Server'])
import configparser 
import os

class Configuration:
    def __init__(self):
        config_file = 'app/config/config.ini'
        if not os.path.exists(config_file):
            raise FileNotFoundError("Configuration file not found")
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_config_value(self, section, key):
        return self.config[section][key]
    
    def get_all_values_result(self):
        result = ("Configuration File Parser Results:\n")
        for section in self.config.sections():
            result += (f"{section}:\n")
            for key, value in self.config.items(section):
                result += (f"- {key}: {value}\n")
        return result

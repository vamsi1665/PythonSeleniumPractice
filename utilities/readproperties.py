import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "..", "Configurations", "config.ini")
config.read(os.path.abspath(config_path))


class Readconfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL').strip()
        return url

    @staticmethod
    def getusername():
        username = config.get('common info', 'username').strip()
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password').strip()
        return password

print("Config loaded from:", os.path.abspath(config_path))
print("Available sections:", config.sections())

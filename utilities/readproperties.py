import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class Readconfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common data','baseURL')
        return url

    @staticmethod
    def getuseremail():
        username = config.get('common data', 'useremail')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common data', 'password')
        return password

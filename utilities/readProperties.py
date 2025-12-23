import configparser
config = configparser.ConfigParser(interpolation=None)
config.read('.\\Configuration\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url = config.get('common info', 'BaseURL')
        return url

    @staticmethod
    def getApplicationusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getApplicationpassword():
        password = config.get('common info', 'password')
        return password

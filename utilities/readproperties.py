import configparser
config=configparser.RawConfigParser()
config.read("Configurations/confi.jh")

class ReadConfig():
    @staticmethod
    def getWebURL():
        url=config.get('Common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('Common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Common info', 'password')
        return password

